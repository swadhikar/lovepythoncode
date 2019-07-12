from json import dumps

# Database of cars and their origin nations
cars_country = {
    'General Motors': 'USA',
    'Volkswagen': 'Germany',
    'Honda': 'Japan'
}

# Database of aircrafts and their origin nations
aircrafts_country = {
    'Boeing': 'USA',
    'Hindustan aircraft': 'India',
    'Energia': 'Russia'
}

merged_content = {**cars_country, **aircrafts_country}
formatted_str = dumps(merged_content, indent=2)    # print dict elegantly looking using json.dumps ()
print(formatted_str)

# {
#   "General Motors": "USA",
#   "Volkswagen": "Germany",
#   "Honda": "Japan",
#   "Boeing": "USA",
#   "Hindustan aircraft": "India",
#   "Energia": "Russia"
# }
