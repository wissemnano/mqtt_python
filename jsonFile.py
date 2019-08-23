import json

#direct read file
dataTest = json.load(open('test.json'))
print(dataTest)



fileName = "test.json"

with open(fileName, 'r') as json_data:
    data = json.load(json_data)
    
print (data)

data_json = 'age'
number = 12

with open(fileName, 'w') as outfiline:
    json.dump(data_json, outfiline)
    json.dump(":", outfiline)
    json.dump(number, outfiline)