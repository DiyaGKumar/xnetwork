# Once you run app.py you'll find a data folder with JSON files
import json
import csv
import os

# Directory containing JSON files
json_directory = 'data/1510499080564211714'  # Replace with the actual directory path 

# Path to the output CSV file
csv_file_path = 'location.csv'  # Replace with the desired output path

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through all JSON files in the directory
    for filename in os.listdir(json_directory):
        if filename.endswith('.json'):
            json_file_path = os.path.join(json_directory, filename)
            
            try:
                # Load JSON data from the file
                with open(json_file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                # Navigate through the nested structure to get to 'entries'
                timeline = data.get('data', {}).get('user', {}).get('result', {}).get('timeline', {}).get('timeline', {})
                instructions = timeline.get('instructions', [])
                
                entries = []
                for instruction in instructions:
                    if instruction.get('type') == 'TimelineAddEntries':
                        entries = instruction.get('entries', [])
                        break
                
                # Traverse the JSON data to extract user names and locations
                for entry in entries:
                    content = entry.get('content', {})
                    item_content = content.get('itemContent', {})
                    user_results = item_content.get('user_results', {})
                    user_info = user_results.get('result', {})
                    
                    if user_info:
                        name = user_info.get('legacy', {}).get('name', 'No name provided')
                        location = user_info.get('legacy', {}).get('location', 'No location provided')
                        
                        # Write the data to the CSV file
                        writer.writerow({'Name': name, 'Location': location})
            
            except Exception as e:
                print(f"Error processing file {filename}: {str(e)}")

print("Data extraction complete. Check the CSV file for results.")