customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
# print(customer["name1"]) # Error key and case sensitive does not exist

print(customer.get("Name", "Karan "))  # Does not throw error even if key does not exist gives NONE

customer["Add_At_Runtime"] = "something_stupid"

print(customer)
