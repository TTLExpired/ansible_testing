import json

with open('city_list.json') as f:
    city_list = json.load(f)

# Some variables
city_dict = {}
city_list_modified = []

for key in city_list:
    city_dict['id'] = key['id']
    city_dict['city'] = key['name']
    city_dict['country'] = key['country']
    city_list_modified.append(city_dict)
    city_dict = {}

with open('city_list_trimmed', 'w') as outfile:
    outfile.write(json.dumps(city_list_modified, indent=2))