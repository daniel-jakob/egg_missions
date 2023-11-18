from PIL import Image, ImageDraw, ImageFont
import os

artifacts_output = [
	{'occurrences': 5, 'name': 'QUANTUM_METRONOME', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 95, 'name': 'BOOK_OF_BASAN', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 31, 'name': 'AURELIAN_BROOCH', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 169, 'name': 'TAU_CETI_GEODE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 15, 'name': 'TUNGSTEN_ANKH', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 46, 'name': 'VIAL_MARTIAN_DUST', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 23, 'name': 'NEODYMIUM_MEDALLION', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 56, 'name': 'SHIP_IN_A_BOTTLE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 50, 'name': 'GOLD_METEORITE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 59, 'name': 'PROPHECY_STONE_FRAGMENT', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 35, 'name': 'DILITHIUM_MONOCLE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 14, 'name': 'BOOK_OF_BASAN', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 20, 'name': 'BEAK_OF_MIDAS', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 54, 'name': 'MERCURYS_LENS', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 80, 'name': 'TACHYON_DEFLECTOR', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 109, 'name': 'SOLAR_TITANIUM', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 63, 'name': 'CLARITY_STONE_FRAGMENT', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 7, 'name': 'THE_CHALICE', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 44, 'name': 'PHOENIX_FEATHER', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 105, 'name': 'LIGHT_OF_EGGENDIL', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 38, 'name': 'THE_CHALICE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 14, 'name': 'BEAK_OF_MIDAS', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 3, 'name': 'AURELIAN_BROOCH', 'level': 'NORMAL', 'rarity': 'EPIC'},
	{'occurrences': 33, 'name': 'PUZZLE_CUBE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 46, 'name': 'DILITHIUM_MONOCLE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 49, 'name': 'TUNGSTEN_ANKH', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 20, 'name': 'TITANIUM_ACTUATOR', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 44, 'name': 'PHOENIX_FEATHER', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 10, 'name': 'MERCURYS_LENS', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 24, 'name': 'QUANTUM_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 61, 'name': 'LUNAR_TOTEM', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 201, 'name': 'GOLD_METEORITE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 13, 'name': 'SOUL_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 45, 'name': 'CARVED_RAINSTICK', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 48, 'name': 'INTERSTELLAR_COMPASS', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 52, 'name': 'CARVED_RAINSTICK', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 11, 'name': 'LUNAR_TOTEM', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 4, 'name': 'QUANTUM_METRONOME', 'level': 'LESSER', 'rarity': 'RARE'},
	{'occurrences': 23, 'name': 'QUANTUM_METRONOME', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 22, 'name': 'TACHYON_DEFLECTOR', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 21, 'name': 'LIFE_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 25, 'name': 'LUNAR_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 24, 'name': 'CLARITY_STONE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 24, 'name': 'DILITHIUM_MONOCLE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 8, 'name': 'PUZZLE_CUBE', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 42, 'name': 'NEODYMIUM_MEDALLION', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 24, 'name': 'TACHYON_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 18, 'name': 'MERCURYS_LENS', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 55, 'name': 'ORNATE_GUSSET', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 7, 'name': 'PROPHECY_STONE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 16, 'name': 'LIGHT_OF_EGGENDIL', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 12, 'name': 'PUZZLE_CUBE', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 44, 'name': 'SHIP_IN_A_BOTTLE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 21, 'name': 'INTERSTELLAR_COMPASS', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 12, 'name': 'THE_CHALICE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 53, 'name': 'TITANIUM_ACTUATOR', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 24, 'name': 'TERRA_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 23, 'name': 'PHOENIX_FEATHER', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 55, 'name': 'BEAK_OF_MIDAS', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 11, 'name': 'LIFE_STONE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 37, 'name': 'QUANTUM_METRONOME', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 17, 'name': 'TUNGSTEN_ANKH', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 29, 'name': 'SOLAR_TITANIUM', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 6, 'name': 'CLARITY_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 4, 'name': 'CARVED_RAINSTICK', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 37, 'name': 'QUANTUM_METRONOME', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 14, 'name': 'SHIP_IN_A_BOTTLE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 12, 'name': 'NEODYMIUM_MEDALLION', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 11, 'name': 'VIAL_MARTIAN_DUST', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 23, 'name': 'SHELL_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 57, 'name': 'DEMETERS_NECKLACE', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 23, 'name': 'THE_CHALICE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 5, 'name': 'LIGHT_OF_EGGENDIL', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 39, 'name': 'AURELIAN_BROOCH', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 14, 'name': 'TUNGSTEN_ANKH', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 24, 'name': 'DEMETERS_NECKLACE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 11, 'name': 'ORNATE_GUSSET', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 49, 'name': 'TITANIUM_ACTUATOR', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 4, 'name': 'AURELIAN_BROOCH', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 9, 'name': 'BEAK_OF_MIDAS', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 12, 'name': 'VIAL_MARTIAN_DUST', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 11, 'name': 'QUANTUM_STONE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 1, 'name': 'QUANTUM_METRONOME', 'level': 'NORMAL', 'rarity': 'EPIC'},
	{'occurrences': 2, 'name': 'TUNGSTEN_ANKH', 'level': 'GREATER', 'rarity': 'RARE'},
	{'occurrences': 4, 'name': 'INTERSTELLAR_COMPASS', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 2, 'name': 'SHELL_STONE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 5, 'name': 'MERCURYS_LENS', 'level': 'LESSER', 'rarity': 'RARE'},
	{'occurrences': 9, 'name': 'TERRA_STONE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 4, 'name': 'THE_CHALICE', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 4, 'name': 'LIGHT_OF_EGGENDIL', 'level': 'LESSER', 'rarity': 'RARE'},
	{'occurrences': 13, 'name': 'TAU_CETI_GEODE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 1, 'name': 'THE_CHALICE', 'level': 'NORMAL', 'rarity': 'EPIC'},
	{'occurrences': 3, 'name': 'TITANIUM_ACTUATOR', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 12, 'name': 'DILITHIUM_STONE', 'level': 'LESSER', 'rarity': 'COMMON'},
	{'occurrences': 4, 'name': 'ORNATE_GUSSET', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 6, 'name': 'PHOENIX_FEATHER', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 3, 'name': 'DEMETERS_NECKLACE', 'level': 'GREATER', 'rarity': 'RARE'},
	{'occurrences': 12, 'name': 'DILITHIUM_STONE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 10, 'name': 'ORNATE_GUSSET', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 5, 'name': 'SOUL_STONE', 'level': 'INFERIOR', 'rarity': 'COMMON'},
	{'occurrences': 1, 'name': 'NEODYMIUM_MEDALLION', 'level': 'GREATER', 'rarity': 'RARE'},
	{'occurrences': 2, 'name': 'PUZZLE_CUBE', 'level': 'GREATER', 'rarity': 'RARE'},
	{'occurrences': 4, 'name': 'INTERSTELLAR_COMPASS', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 1, 'name': 'THE_CHALICE', 'level': 'GREATER', 'rarity': 'EPIC'},
	{'occurrences': 3, 'name': 'AURELIAN_BROOCH', 'level': 'GREATER', 'rarity': 'RARE'},
	{'occurrences': 3, 'name': 'TUNGSTEN_ANKH', 'level': 'LESSER', 'rarity': 'RARE'},
	{'occurrences': 2, 'name': 'DEMETERS_NECKLACE', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 2, 'name': 'NEODYMIUM_MEDALLION', 'level': 'LESSER', 'rarity': 'RARE'},
	{'occurrences': 3, 'name': 'LUNAR_TOTEM', 'level': 'GREATER', 'rarity': 'RARE'},
	{'occurrences': 3, 'name': 'SHIP_IN_A_BOTTLE', 'level': 'NORMAL', 'rarity': 'RARE'},
	{'occurrences': 1, 'name': 'QUANTUM_METRONOME', 'level': 'GREATER', 'rarity': 'COMMON'},
	{'occurrences': 2, 'name': 'LUNAR_STONE', 'level': 'NORMAL', 'rarity': 'COMMON'},
	{'occurrences': 1, 'name': 'INTERSTELLAR_COMPASS', 'level': 'GREATER', 'rarity': 'RARE'},
	{'occurrences': 1, 'name': 'LUNAR_TOTEM', 'level': 'GREATER', 'rarity': 'EPIC'},
	{'occurrences': 1, 'name': 'NEODYMIUM_MEDALLION', 'level': 'NORMAL', 'rarity': 'EPIC'},
	{'occurrences': 1, 'name': 'THE_CHALICE', 'level': 'LESSER', 'rarity': 'EPIC'},
	{'occurrences': 1, 'name': 'SOUL_STONE', 'level': 'NORMAL', 'rarity': 'COMMON'},
]

# Map from word form to number form for the "level" field
level_mapping = {"INFERIOR": 1, "LESSER": 2, "NORMAL": 3, "GREATER": 4, "SUPERIOR": 5}

# Define custom sorting orders
rarity_order = {"COMMON": 3, "RARE": 2, "EPIC": 1, "LEGENDARY": 0}
level_order = {"INFERIOR": 4, "LESSER": 3, "NORMAL": 2, "GREATER": 1, "SUPERIOR": 0}
type_order = {"artifact": 1, "stone": 2, "ingredient": 3}

# Convert the level field in sorted_output to number form
# Convert the 'name' field to lowercase and the 'level' field to number form in sorted_output
for item in artifacts_output:
	item['name'] = item['name'].lower()
	item['level'] = level_mapping.get(item['level'], 999)  # Using 999 as a default if level is not in the mapping
	
	# Rename 'neodymium' to 'neo'
	if 'neodymium' in item['name']:
		item['name'] = 'neo_medallion'
	if 'light_of_eggendil' in item['name']:
		item['name'] = 'light_eggendil'
	item['type'] = 'stone' if 'stone' in item['name'] else 'artifact'
	if 'solar' in item['name'] or 'meteorite' in item['name'] or 'geode' in item['name']:
		item['type'] = 'ingredient'

	#to fix level of stones and their fragments

	if item['name'] == 'prophecy_stone' and item['level'] == 3: item['level'] = 4
	if item['name'] == 'prophecy_stone' and item['level'] == 2: item['level'] = 3
	if item['name'] == 'prophecy_stone' and item['level'] == 1: item['level'] = 2
	
	if item['name'] == 'clarity_stone' and item['level'] == 3: item['level'] = 4
	if item['name'] == 'clarity_stone' and item['level'] == 2: item['level'] = 3
	if item['name'] == 'clarity_stone' and item['level'] == 1: item['level'] = 2
	
	

	item['name'] = item['name'].replace('_fragment', '')

# Define a custom sorting key function
def custom_sort(item):
	return (
		type_order.get(item['type'], float('inf')),  # Sort by type
		rarity_order.get(item['rarity'], float('inf')),  # Sort by rarity
		item['name'],  # Then sort by name
		-item['level']  # Finally, sort by level
	)

# Sort the list using the custom sorting key
sorted_output = sorted(artifacts_output, key=custom_sort)


# Print the sorted result
for item in sorted_output:
	print(item)

#sys.exit()

images_folder = "book/"

# Assuming each image is a square of size 100x100 pixels
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
	
	if item['rarity'] != "COMMON":
		circle_color = circle_colors.get(item['rarity'])
		# Calculate the center and radius of the ellipse
		center_x = (position[0] * 2 + image_size[0]) // 2
		center_y = (position[1] * 2 + image_size[1]) // 2
		radius = min(image_size) // 2.25  # Use the minimum of width and height as the radius

		#print(position[0], position[0], image_size[0])

		# Draw the ellipse with the specified radius
		draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], fill=circle_color)

	# Paste the image onto the final image
	final_image.paste(img, position, mask=img)

	if item['occurrences'] > 1:
		circle_color = (156, 163, 175)
		# Calculate the center and radius of the ellipse
		center_x = (position[0] + position[0] + image_size[0]) // 2 + image_size[0] // 3
		center_y = (position[1] + position[1] + image_size[1]) // 2 + image_size[0] // 3
		radius = min(image_size) // 8  # Use the minimum of width and height as the radius

		# Draw the ellipse with the specified radius
		draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], fill=circle_color)

		#text_size = draw.textsize(str(item['occurrences']), font=font)

		draw.text([center_x, center_y], str(item['occurrences']), anchor="mm", font=font, fill="black")

# Save or display the final image
final_image.save("output_image.png")
final_image.show()