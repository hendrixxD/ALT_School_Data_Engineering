import os
import csv
import json

# Function to process JSON files and write data to CSV
def process_json_to_csv(json_folder, csv_filename, data_key, json_fields):
    csv_file_path = f'{csv_filename}.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_fields)
        writer.writeheader()

        for filename in os.listdir(json_folder):
            if filename.endswith('.json'):
                with open(os.path.join(json_folder, filename), 'r') as json_file:
                    data = json.load(json_file)
                    payload = data[data_key]
                    payload['event_id'] = data['metadata']['event_id']  # Extract event_id from metadata
                    payload['event_at'] = data['metadata']['event_at']  # Extract event_at from metadata
                    payload['type'] = data['metadata']['type']          # Extract event_at from metadata
                    writer.writerow(payload)

# Path to the folders containing JSON files
users_json_folder = '/home/hendrixxdiddy/DEV/ALT_School_Data_Engineering/learning_circle_assessement/1st_assessment/events/users'
cards_json_folder = '/home/hendrixxdiddy/DEV/ALT_School_Data_Engineering/learning_circle_assessement/1st_assessment/events/cards'

# Specify JSON field names for users and cards
users_fields = ['id', 'name', 'address', 'job', 'score', 'type', 'event_at', 'event_id']
cards_fields = ['id', 'user_id', 'created_by_name', 'updated_at', 'created_at', 'active', 'type', 'event_at', 'event_id']

# Generate users.csv
process_json_to_csv(users_json_folder, 'users', 'payload', users_fields)

# Generate cards.csv
process_json_to_csv(cards_json_folder, 'cards', 'payload', cards_fields)

print("CSV files generated successfully.")
