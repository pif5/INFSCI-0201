
import json

# creating json object
people_string = '''
{
    "people": [
        {
            "name": "John",
            "phone": "615",
            "has_l": false
        }
    ]
}
'''

# Parse the JSON string into a Python dictionary
data = json.loads(people_string)

# Print the resulting dictionary
print(data)

for person in data['people']:
    print(person)
# print out all the in object

new_string= json.dumps(data, indent=2, sort_keys=True) # indent how many space for new line,sort keys= alpahbetical order 



with open( 'name.json') as f:
    data2 = json.load(f)
    
    # reads jason file 
    
for person in data2['people']:
    del person['phone']
## delete number

#converts to json new_string
with open('newname.json', 'w') as f:
    json.dump(data, f, indent=2)
    
    ## created new json list eit our existing 
  
from urllib.request import urlopen  
    
with urlopen("url.json") as response:
    source =response.read()
    
data = json.loads(source) ## makes it into pythong object


    
    
    
    
    