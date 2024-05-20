import json
file_path = '/home/lafesta/Desktop/DAforIT/dataset/Google/Google_OLED_co.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
# Count words with multiple definitions
multiple_definitions_count = 0
words_with_multiple_definitions = []
for entry in data:
    if len(entry['definition']) > 1:
        multiple_definitions_count += 1
        words_with_multiple_definitions.append(entry)
# Display the count of words with multiple definitions
print(multiple_definitions_count)
# Save the data of words with multiple definitions to a new JSON file
output_file_path = '/home/lafesta/Desktop/DAforIT/Words_With_Multiple_Definitions_GoogleOED.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(words_with_multiple_definitions, output_file, ensure_ascii=False, indent=4)

# import json
# file_path = '/home/lafesta/Desktop/DAforIT/dataset/OLED/OLED/OLED_Google_co.json'
# with open(file_path, 'r', encoding='utf-8') as file:
#     data = json.load(file)
# # Count words with multiple definitions
# multiple_definitions_count = 0
# words_with_multiple_definitions = []
# for entry in data:
#     if len(entry['definition']) > 1:
#         multiple_definitions_count += 1
#         words_with_multiple_definitions.append(entry)
# # Display the count of words with multiple definitions
# print(multiple_definitions_count)
# # Save the data of words with multiple definitions to a new JSON file
# output_file_path = '/home/lafesta/Desktop/DAforIT/Words_With_Multiple_Definitions_OLED.json'
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     json.dump(words_with_multiple_definitions, output_file, ensure_ascii=False, indent=4)