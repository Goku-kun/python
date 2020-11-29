import json
# The json module will help us convert from and convert to JSON.

# The equivalent datatypes of python in JSON can be described as follows:
"""
Python      --      JSON
dict                object
list                Array
tuple               Array
int, float, long    number
True                true
False               false
str                 string
None                null
"""

# python object to JSON conversion

person = {"name":"Goku", "age": "immortal", "hasChildren":True, "forms": 6,"titles":["Saiyan", "Ultra Instinct", "Super Saiyan", "Martial Artist"]}

personJSON = json.dumps(person, indent=4, sort_keys=True) # the dump command converts an object to a JSON object but dump s command will convert a string to a json object
print(personJSON)

# writing a JSON object ot a .json file
with open("person.json", "w") as file:
    json.dump(person, file, indent=2)
    file.close()


# JSON to python object conversion

goku = json.loads(personJSON) # look at the hasChildren attribute, the True has come back to the python format.
print(goku)

# READING a .json file and making a python object(dictionary) out of it
with open("person.json",'r') as file:
    fileJSONread = json.load(file)
print(sorted(fileJSONread.items(), key= lambda x: x[0]))