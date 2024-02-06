import googlemaps
from datetime import datetime
import pandas as pd
import csv
import secret_key as key

gmaps = googlemaps.Client(key=key.k)

def calculate_location_info(block, road, house):
    # Perform your calculations here based on block, road, and house

    # Create the address string using variables

    address = f'Block-{block},Road-{road},House-{house}, Bashundhara R/A, Dhaka'
    
    # Geocoding an address
    geocode_result = gmaps.geocode(address) 

    # for detaching the attributes from geocode_result

    geometry = geocode_result[0].get('geometry', {})

    location = geometry.get('location', {})
    location_type = geometry.get('location_type', {})
    viewport = geometry.get('viewport', {})

    return location, location_type, viewport


# Read the CSV file
file_path = 'output.csv' 
data = pd.read_csv(file_path)

# Store the records in a list of dictionaries
records_list = []
for index, row in data.iterrows():
    record = {
        'order_id': row['order_id'],
        'billing1_block': row['billing1_block'],
        'billing1_road': row['billing1_road'],
        'billing1_house': row['billing1_house'],
        'billing2_block': row['billing2_block'],
        'billing2_road': row['billing2_road'],
        'billing2_house': row['billing2_house']
    }
    records_list.append(record)

# Displaying the first few records
# print(records_list[0]['billing1_block'])  # Displaying the first 5 records as an example

location_info_list = []
for record in records_list:
    id = record['order_id']

    billing1_block = record['billing1_block']
    billing1_road = record['billing1_road']
    billing1_house = record['billing1_house']

    billing2_block = record['billing2_block']
    billing2_road = record['billing2_road']
    billing2_house = record['billing2_house']

    # Calculate location information using the function
    if not(billing1_block=='_' and billing1_road=='_' and billing1_house=='_'):
        location1, location_type1, viewport1 = calculate_location_info(billing1_block, billing1_road, billing1_house)
    else:
        location1, location_type1, viewport1 = '_','_','_'

    # Calculate location information using the function
    if not(billing2_block=='_' and billing2_road=='_' and billing2_house=='_'):
        location2, location_type2, viewport2 = calculate_location_info(billing2_block, billing2_road, billing2_house)
    else:
        location2, location_type2, viewport2 = '_','_','_'

    # Create a dictionary for location information
    location_info = {
        'order_id' : id,

        'billing1_location': location1,
        'billing1_location_type': location_type1,
        'billing1_viewport': viewport1,

        'billing2_location': location2,
        'billing2_location_type': location_type2,
        'billing2_viewport': viewport2,

        'shipping1_location': location1,
        'shipping1_location_type': location_type1,
        'shipping1_viewport': viewport1,

        'shipping2_location': location2,
        'shipping2_location_type': location_type2,
        'shipping2_viewport': viewport2,
    }

    # print(location_info)

    # Append this dictionary to the location_info_list
    location_info_list.append(location_info)


    
file_name = 'output_location_info.csv'

# Define the column headers
headers = [
    'order_id',
    'billing1_location',
    'billing1_location_type',
    'billing1_viewport',
    'billing2_location',
    'billing2_location_type',
    'billing2_viewport',
    'shipping1_location',
    'shipping1_location_type',
    'shipping1_viewport',
    'shipping2_location',
    'shipping2_location_type',
    'shipping2_viewport'
]

# Writing the data to a CSV file
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    # Write the header row
    writer.writeheader()

    # Write data from location_info_list to the CSV file
    for item in location_info_list:
        writer.writerow(item)


