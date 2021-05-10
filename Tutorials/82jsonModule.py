import json

'''
loads - str to dict
dumps - dict to json
load - read json to dict in file
dump - write dict in file to str
'''

#  -- LOADS -- 
data = '{"var1":"harry", "var2":"ars"}'  #format important  '{"key":"value", "key":"value"}'  with no comments
print(data)
# print(data['var1'])  # Gives ERROR as string

parse = json.loads(data)       
print(parse)
print(type(parse))
print(parse['var1'])

# -- DUMPS -- 
#  MAKING JS COMAPATIBLE --
details = {
    "Name": "Harry",
    "Job": ("Programmer", "Coder", 540),
    "Fruits": ["Apple", "Banana", "Grapes"],
    "isBad": False
}
print(details)
detailsNew = json.dumps(details, indent=4 ,sort_keys=False)          # dict to json
print(detailsNew)

detailsNew = json.dumps(details, indent=4 ,sort_keys=True)          # dict to json
print(detailsNew)

#  -- LOAD --  
with open('82data2.json', 'r') as e:
    x = json.load(e)
    print(x['Name'])
    print(x)


#  DUMP
with open('82data2.json', 'a') as e:
    e.write(detailsNew)
    #  OR
    # json.dump(detailsNew, e)
