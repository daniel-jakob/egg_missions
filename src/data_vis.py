from PIL import Image, ImageDraw, ImageFont
import json
import os

with open("data.json", "r") as f:
	artifacts_output = json.load(f)

# Map from word form to number form for the "level" field
level_mapping = {"INFERIOR": 1, "LESSER": 2, "NORMAL": 3, "GREATER": 4, "SUPERIOR": 5}

# Define custom sorting orders
rarity_order = {"COMMON": 1, "RARE": 2, "EPIC": 3, "LEGENDARY": 4}
type_order = {"artifact": 1, "stone": 2, "ingredient": 3}

fragment_level_mapping = {1: 2, 2: 3, 3: 4}
# Convert the level field in sorted_output to number form
# Convert the 'name' field to lowercase and the 'level' field to number form in sorted_output
for item in artifacts_output:
	item['name'] = item['name'].lower()
	item['level'] = level_mapping.get(item['level'], 999)  # Using 999 as a default if level is not in the mapping
	
	# Type field creation. Used for sorting artfacts->stones->ingredients
	item['type'] = 'stone' if 'stone' in item['name'] else 'artifact'
	if 'solar' in item['name'] or 'meteorite' in item['name'] or 'geode' in item['name']:
		item['type'] = 'ingredient'

	#to fix level of stones and their fragments
	if item['name'] in {'prophecy_stone', 'clarity_stone', 'quantum_stone', 'life_stone'}:
		print(item['name'], item['level'] )
		# Use get to handle cases where item_level is not present in the mapping
		new_level = fragment_level_mapping.get(item.get('level'))
		if new_level is not None:
			item['level'] = new_level
		print(item['name'], item['level'] )
	
	
	item['name'] = item['name'].replace('_fragment', '')

# Define a custom sorting key function
def custom_sort(item):
	return (
		type_order.get(item['type'], float('inf')),  # Sort by type
		-rarity_order.get(item['rarity'], float('inf')),  # Sort by rarity (reversed)
		item['name'],  # Then sort by name
		-item['level']  # Finally, sort by level (reversed)
	)

# Sort the list using the custom sorting key
sorted_output = sorted(artifacts_output, key=custom_sort)


# Print the sorted result
# for item in sorted_output:
# 	print(item)

images_folder = "images/"

# Assuming each image is a square of size 
image_size = (128, 128)

# Define colors for the circles based on rarity
circle_colors = {
	"RARE": (179, 255, 255),  # Blue for "RARE"
	"EPIC": (255, 64, 255),  # Purple for "EPIC"
	"LEGENDARY": (255, 254, 65),  # Yellow for "LEGENDARY"
}


# Number of images per row
images_per_row = 10

# Create a new image with a grey background

background_color = (50, 50, 50)  # Grey color 

num_images = len(sorted_output)
num_rows = (num_images + images_per_row - 1) // images_per_row
final_image_size = (image_size[0] * images_per_row, image_size[1] * num_rows)
final_image = Image.new("RGB", final_image_size, background_color + (0,))
draw = ImageDraw.Draw(final_image)

# Get the default font with the specified size
font_size = 19
font = ImageFont.load_default()
font = font.font_variant(size=font_size)

# Paste each image into the final image
for i, item in enumerate(sorted_output):
	image_name = f"{item['name']}_{item['level']}.png"
	image_path = os.path.join(images_folder, image_name)

	# Open the image
	try:
		img = Image.open(image_path)
	except FileNotFoundError:
		print(f"Image not found: {image_name}")
		continue

	# Calculate the position to paste the image
	col = i % images_per_row
	row = i // images_per_row
	position = (col * image_size[0], row * image_size[1])


	# If rare, epic, legendary, put coloured circle behind artifact image
	if item['rarity'] != "COMMON":
		circle_color = circle_colors.get(item['rarity'])
		# Calculate the center and radius of the ellipse
		center_x = (position[0] * 2 + image_size[0]) // 2
		center_y = (position[1] * 2 + image_size[1]) // 2
		radius = min(image_size) // 2.25  # Use the minimum of width and height as the radius


		# Draw the ellipse with the specified radius
		draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], fill=circle_color)

	# Paste the image onto the final image, preserving the transparacny
	final_image.paste(img, position, mask=img)

	# Grey circle with number of occurrences in bottom right
	if item['occurrences'] > 1:
		circle_color = (156, 163, 175)
		# Calculate the center and radius of the ellipse
		center_x = (position[0] + position[0] + image_size[0]) // 2 + image_size[0] // 3
		center_y = (position[1] + position[1] + image_size[1]) // 2 + image_size[0] // 3
		radius = min(image_size) // 8  # Use the minimum of width and height as the radius

		# Draw the ellipse with the specified radius
		draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], fill=circle_color)


		draw.text([center_x, center_y], str(item['occurrences']), anchor="mm", font=font, fill="black")

# Save or display the final image
final_image.save("output_image.png")
final_image.show()