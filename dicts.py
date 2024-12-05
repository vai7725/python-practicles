# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Accessing values
name = my_dict["name"]
age = my_dict.get("age")

# Adding or updating key-value pairs
my_dict["email"] = "john@example.com"
my_dict["age"] = 26

# Removing a key-value pair
del my_dict["city"]

# Checking if a key exists
has_email = "email" in my_dict

# Iterating through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()

# Copying the dictionary
copied_dict = my_dict.copy()

# Clearing the dictionary
my_dict.clear()

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Has email: {has_email}")
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Copied dictionary: {copied_dict}")
