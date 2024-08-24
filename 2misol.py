import json
malumot={
    "first_name":"John",
    "last_name":"Doe",
    "age":34,
    "student":False,
    "worker":True
}

file=open("malumot.json","w")

data=json.dumps(malumot)
file.write(data)

file.close()

file=open("malumot.json","r")
data=json.loads("malumot.txt")
print(file.read(data))
