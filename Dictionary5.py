dictionary= {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"

}

rename = ["city"]
old_key = dictionary["city"]
dictionary["location"] = old_key

del dictionary["city"]
print(dictionary)
