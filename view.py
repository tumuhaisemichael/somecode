import json

# Load the scraped data
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the data in a readable format
print(json.dumps(data, indent=4))

# Analyze the data (example: print number of links)
print(f"Total number of links: {len(data['links'])}")
