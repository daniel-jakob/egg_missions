import requests
import ei_pb2
import base64
from google.protobuf.json_format import MessageToJson
from itertools import islice
import os
import json
import time 


# SET YOUR INFO HERE!

EGG_API_KEY = 'EI1234567890123456' # Put your Egg, Inc. ID here
num_ships = 1 # The number of ships you want to ask the API for 

# If wanting to visualise a specific type of ship 
# ['one', 'nine', 'heavy', 'bcr', 'quintillion', 'cornish', 'galeggtica', 'defihent', 'voyegger', 'henerprise']
# [short, standard, extended]
# default is None. Searches for all types and lengths
ship_type = None
ship_length = None

#ship_type = 'nine'
#ship_length = 'short'


ei_id = os.environ.get('EGG_API_KEY', EGG_API_KEY) # can set an environ. variable if you want, default is input above

# Making first contact request to API. This is to get the list of mission IDs
first_contact_request = ei_pb2.EggIncFirstContactRequest()
first_contact_request.ei_user_id = ei_id
first_contact_request.client_version = 61

url = 'https://www.auxbrain.com/ei/bot_first_contact'
data = { 'data' : base64.b64encode(first_contact_request.SerializeToString()).decode('utf-8') }
response = requests.post(url, data = data)

first_contact_response = ei_pb2.EggIncFirstContactResponse()
first_contact_response.ParseFromString(base64.b64decode(response.text))


# Need to sort the returned missions by start date, newest first
sorted_mission_archive = sorted(
	first_contact_response.backup.artifacts_db.mission_archive,
	key=lambda x: x.start_time_derived, reverse=True  # Assuming 0 as default value if 'epoch_time' is missing
)

#print (sorted_mission_archive)

length_translation = {
	"short": 0,
	"standard": 1,
	"extended": 2,
}
translated_length = length_translation.get(ship_length, ship_length)

options = ['one', 'nine', 'heavy', 'bcr', 'quintillion', 'cornish', 'galeggtica', 'defihent', 'voyegger', 'henerprise']

# Check if ship_type is not None and is in the options list
if ship_type is not None and ship_type in options:
    translated_type = options.index(ship_type)
else:
    translated_type = None  # or set to a default value, depending on your requirements


# Filter by "ship" and/or "duration_type" based on which variable is not None
filtered_missions = filter(
    lambda mission: (translated_type is None or mission.ship == translated_type) and
                    (translated_length is None or mission.duration_type == translated_length),
    sorted_mission_archive
)
# Convert the filtered result back to a list
filtered_missions_list = list(filtered_missions)


artifacts_json_simple = []
i = 0
# Asking API for mission contents of num_ship number of missions
for mission_archive in islice(filtered_missions_list, num_ships): # Taking num_ship number of missions

	# API request and response
	mission_request = ei_pb2.MissionRequest()
	mission_request.ei_user_id = ei_id
	mission_request.info.identifier = mission_archive.identifier

	url = 'https://www.auxbrain.com/ei_afx/complete_mission'
	data = { 'data' : base64.b64encode(mission_request.SerializeToString()).decode('utf-8') }
	response = requests.post(url, data = data)

	authenticated_message = ei_pb2.AuthenticatedMessage()
	authenticated_message.ParseFromString(base64.b64decode(response.text))

	mission_response = ei_pb2.CompleteMissionResponse()
	mission_response.ParseFromString(authenticated_message.message)
	  
	# Converting response to JSON
	artifacts_json = [MessageToJson(spec) for spec in mission_response.artifacts]

	i=i+1

	# New structure with only the info we need
	for item in artifacts_json:
		item = json.loads(item)
		simplified_item = {
		"name": item["spec"]["name"],
		"level": item["spec"]["level"],
		"rarity": item["spec"]["rarity"]
		}
		artifacts_json_simple.append(simplified_item)
	
	# Pause for a second between API calls to avoid overloading
	time.sleep(1)
	print('Ship number', i, 'scanned')

# Removing duplicate values and keeping tally of number of duplicates to place in "occurrences" field for each item
occurrences_dict = {}

for item in artifacts_json_simple:
	# Convert the list of key-value pairs into a tuple
	item_key = tuple(item.items())
	occurrences_dict[item_key] = occurrences_dict.get(item_key, 0) + 1

# Generate the new output with occurrences
new_output = [{'occurrences': count, **dict(key)} for key, count in occurrences_dict.items()]

with open("data.json", "w") as f:
	json.dump(new_output, f)

# Uncomment to print the result
# for item in new_output:
# 	print(item)