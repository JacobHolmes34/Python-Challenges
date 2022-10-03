simpleDict = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city": "New York"

}
keysToRemove = ["name", "salary"]
del simpleDict["name"]
del simpleDict["salary"]
print(simpleDict)
