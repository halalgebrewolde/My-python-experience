customer={
    "name":"John Smith",
    "age":30,
    "is_verified":True
    }
print(customer["name"])
#print(customer["birthdate"])
print(customer.get("birthdate","Jan 1 1982"))
customer["name"]="Jack"
print(customer["name"])