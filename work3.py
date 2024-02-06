import re
import csv
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'data.csv'

strings_to_concat = []

billing1 = []
billing2 = []
shipping1 = []
shipping2 = []
order_id = []
pattern = r'(\w+_address_\d+):([^%]+)'
# Open the CSV file for reading
with open(csv_file, 'r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values, and you can access them by index
        # For example, to print the first and second columns of each row:
        strings_to_concat.append(row[2])

        if(row[0] != "order_id"):
            order_id.append(row[0])
        
            address_components = re.findall(pattern, row[2])

            address_dict = {}

            # Process the address components and store them in the dictionary
            for key, value in address_components:
                address_dict[key] = value

            #Print the separated addresses
            bill1_flag = 0
            bill2_flag = 0
            ship1_flag = 0
            ship2_flag = 0
            for key, value in address_dict.items():
                #print(f"{key}: {value.strip()}")
                if key == "billing_address_1":
                    billing1.append(value.strip())
                    bill1_flag = 1
                elif key == "billing_address_2":
                    billing2.append(value.strip())
                    bill2_flag = 1
                elif key == "shipping_address_1":
                    shipping1.append(value.strip())
                    ship1_flag = 1
                elif key == "shipping_address_2":
                    shipping2.append(value.strip())
                    ship2_flag = 1
            if(bill1_flag == 0):
                billing1.append("_")
            if(bill2_flag == 0):
                billing2.append("_")
            if(ship1_flag == 0):
                shipping1.append("_")
            if(ship2_flag == 0):
                shipping2.append("_")


# print(billing1[1])

# for i in range(0, 5):
#     print(billing1[i])

modified_billing1 = []
modified_billing2 = []
modified_shipping1 = []
modified_shipping2 = []

# patt = r'(?i)(block|house|road)\s*+(No:|no:|NO:|\s*|-)\s*([A-Za-z]|[0-9]+)'

for address in billing1:
    address = address.lower()
    patt = r'(?i)(block|house|road)\s*(No:|no:|NO:|\s*|-|:)\s*([A-Za-z]|[0-9]+)'

    def replace(match):
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address1
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address1 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address1 = ''
    formatted_address = re.sub(patt, replace_and_move, address)


    patt = r'(?i)([A-Za-z]|[0-9]+)\s*(:|no:|No:|NO:|\s*)\s*(road|house|block)'

    def replace(match):
        component = match.group(3).lower()  # Convert to lowercase
        value = match.group(1)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address2
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address2 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address2 = ''
    formatted_address = re.sub(patt, replace_and_move, formatted_address)

    formatted_address = formatted_address1 + formatted_address2
    
    modified_billing1.append(formatted_address)

######################################

for address in billing2:
    address = address.lower()
    patt = r'(?i)(block|house|road)\s*(No:|no:|NO:|\s*|-|:)\s*([A-Za-z]|[0-9]+)'

    def replace(match):
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address1
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address1 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address1 = ''
    formatted_address = re.sub(patt, replace_and_move, address)


    patt = r'(?i)([A-Za-z]|[0-9]+)\s*(:|no:|No:|NO:|\s*)\s*(road|house|block)'

    def replace(match):
        component = match.group(3).lower()  # Convert to lowercase
        value = match.group(1)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address2
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address2 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address2 = ''
    formatted_address = re.sub(patt, replace_and_move, formatted_address)

    formatted_address = formatted_address1 + formatted_address2

    modified_billing2.append(formatted_address)
#############################################################

for address in shipping1:
    address = address.lower()
    patt = r'(?i)(block|house|road)\s*(No:|no:|NO:|\s*|-|:)\s*([A-Za-z]|[0-9]+)'

    def replace(match):
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address1
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address1 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address1 = ''
    formatted_address = re.sub(patt, replace_and_move, address)


    patt = r'(?i)([A-Za-z]|[0-9]+)\s*(:|no:|No:|NO:|\s*)\s*(road|house|block)'

    def replace(match):
        component = match.group(3).lower()  # Convert to lowercase
        value = match.group(1)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address2
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address2 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address2 = ''
    formatted_address = re.sub(patt, replace_and_move, formatted_address)

    formatted_address = formatted_address1 + formatted_address2

    modified_shipping1.append(formatted_address)    

for address in shipping2:
    address = address.lower()
    patt = r'(?i)(block|house|road)\s*(No:|no:|NO:|\s*|-|:)\s*([A-Za-z]|[0-9]+)'

    def replace(match):
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address1
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address1 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address1 = ''
    formatted_address = re.sub(patt, replace_and_move, address)


    patt = r'(?i)([A-Za-z]|[0-9]+)\s*(:|no:|No:|NO:|\s*)\s*(road|house|block)'

    def replace(match):
        component = match.group(3).lower()  # Convert to lowercase
        value = match.group(1)
        value = value + " "
        return f'{component}_{value}'

    def replace_and_move(match):
        global formatted_address2
        component = match.group(1).lower()  # Convert to lowercase
        value = match.group(3)
        value = value + " "
        formatted_address2 += f'{component}_{value}'
        return ''  # Replace with an empty string to remove the matched pattern

    formatted_address2 = ''
    formatted_address = re.sub(patt, replace_and_move, formatted_address)

    formatted_address = formatted_address1 + formatted_address2


    modified_shipping2.append(formatted_address)

# print(len(modified_billing1))
# print(len(modified_billing2))
# print(len(modified_shipping1))
# print(len(modified_shipping2))

# for address in modified_billing1:
#     print(address)


csv_data = []

# block_pattern = re.compile(r'block_([A-Za-z] | [0-9]+)', re.IGNORECASE)
# house_pattern = re.compile(r'house_([A-Za-z] | [0-9]+)', re.IGNORECASE)
# road_pattern = re.compile(r'road_([A-Za-z] | [0-9]+)', re.IGNORECASE)

block_patt = r'(?i)(block_)\s*([A-Za-z]|[0-9]+)'
house_patt = r'(?i)(house_)\s*([A-Za-z]|[0-9]+)'
road_patt = r'(?i)(road_)\s*([A-Za-z]|[0-9]+)'


# def replace(match):
#     component = match.group(1).lower()  # Convert to lowercase
#     value = match.group(2)
#     value = value + " "
#     return f'{component}{value}'

# testing = "block_A road_12 houseA"

# matches = re.findall(block_patt, testing)

# for ent in matches: 
#     print(ent[0] + ent[1]);

# print(matches);

billing1_block = []
billing1_road = []
billing1_house = []



for address in modified_billing1:
    #print(address)
    matches_block = re.findall(block_patt, address)
    matches_road = re.findall(road_patt, address)
    matches_house = re.findall(house_patt, address)
    
    if(len(matches_block) == 0):
        billing1_block.append("_")
    
    if(len(matches_road) == 0):
        billing1_road.append("_")
    
    if(len(matches_house) == 0):
        billing1_house.append("_")

    for ent in matches_block:
        billing1_block.append(ent[1])
    for ent in matches_road:
        billing1_road.append(ent[1])
    for ent in matches_house:
        billing1_house.append(ent[1])

billing2_block = []
billing2_road = []
billing2_house = []

for address in modified_billing2:
    matches_block = re.findall(block_patt, address)
    matches_road = re.findall(road_patt, address)
    matches_house = re.findall(house_patt, address)

    if(len(matches_block) == 0):
        billing2_block.append("_")
    
    if(len(matches_road) == 0):
        billing2_road.append("_")
    
    if(len(matches_house) == 0):
        billing2_house.append("_")
    

    for ent in matches_block:
        billing2_block.append(ent[1])
    for ent in matches_road:
        billing2_road.append(ent[1])
    for ent in matches_house:
        billing2_house.append(ent[1])


shipping1_block = []
shipping1_road = []
shipping1_house = []

for address in modified_shipping1:
    matches_block = re.findall(block_patt, address)
    matches_road = re.findall(road_patt, address)
    matches_house = re.findall(house_patt, address)

    if(len(matches_block) == 0):
        shipping1_block.append("_")
    
    if(len(matches_road) == 0):
        shipping1_road.append("_")
    
    if(len(matches_house) == 0):
        shipping1_house.append("_")
    

    for ent in matches_block:
        shipping1_block.append(ent[1])
    for ent in matches_road:
        shipping1_road.append(ent[1])
    for ent in matches_house:
        shipping1_house.append(ent[1])

shipping2_block = []
shipping2_road = []
shipping2_house = []

for address in modified_shipping2:
    matches_block = re.findall(block_patt, address)
    matches_road = re.findall(road_patt, address)
    matches_house = re.findall(house_patt, address)

    if(len(matches_block) == 0):
        shipping2_block.append("_")
    
    if(len(matches_road) == 0):
        shipping2_road.append("_")
    
    if(len(matches_house) == 0):
        shipping2_house.append("_")

    for ent in matches_block:
        shipping2_block.append(ent[1])
    for ent in matches_road:
        shipping2_road.append(ent[1])
    for ent in matches_house:
        shipping2_house.append(ent[1])


# print(len(billing1_block))
# print(len(billing1_road))
# print(len(billing1_house))
# print(len(billing2_block))
# print(len(billing2_road))
# print(len(billing2_house))
# print(len(shipping1_block))
# print(len(shipping1_road))
# print(len(shipping1_house))
# print(len(shipping2_block))
# print(len(shipping2_road))
# print(len(shipping2_house))



for id, b1_b, b1_r, b1_h , b2_b, b2_r, b2_h, s1_b, s1_r, s1_h , s2_b, s2_r, s2_h in zip(order_id, billing1_block, billing1_road, billing1_house, billing2_block, billing2_road, billing2_house, shipping1_block, shipping1_road, shipping1_house, shipping2_block, shipping2_road, shipping2_house):
    csv_data.append([id, b1_b, b1_r, b1_h, b2_b, b2_r, b2_h, s1_b, s1_r, s1_h , s2_b, s2_r, s2_h])

csv_file_path = 'output.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    csv_writer.writerow(['order_id', 'billing1_block', 'billing1_road', 'billing1_house', 'billing2_block', 'billing2_road', 'billing2_house', 'shipping1_block', 'shipping1_road', 'shipping1_house', 'shipping2_block', 'shipping2_road', 'shipping2_house'])

    # Write data
    csv_writer.writerows(csv_data)

print(f"CSV file '{csv_file_path}' has been created.")