# Returns csv with all followers and their locations (if they have any)
import csv

refined_data = []

# Read and filter the data
with open('location.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    
    for row in reader:
        if len(row) == 2:
            name, location = row
            # Check if location is not empty and not a placeholder
            if location and location.strip() not in ['', 'No location provided']:
                refined_data.append((name, location))

# Write the refined data to a new CSV file
with open('refined.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Location'])  # Write header
    writer.writerows(refined_data)

print(f"Refined data saved to 'refined.csv'")
print(f"Total entries with valid locations: {len(refined_data)}")