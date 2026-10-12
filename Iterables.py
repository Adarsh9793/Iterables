users = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Software Engineer"
}

for key , value in users.items():
    print(key,"->",value)

a , b , c = (1,2,3)

for items in users.keys():
    print(items)

for items in users.values():
    print(items)

for items in [50]:
    print(items)