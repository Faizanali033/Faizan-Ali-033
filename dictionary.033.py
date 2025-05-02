# Creating a dictionary with 10 key-value pairs
my_dict = {
    "name": "Faizan",
    "age": 19,
    "city": "Lahore",
    "country": "Pakistan",
    "profession": "Marketer",
    "hobby": "Reading",
    "favorite_color": "Black",
    "height": 5.5,
    "weight": 69,
    "language": "Urdu"
}

# Applying at least 10 dictionary methods
print("Original Dictionary:", my_dict)

# 1. get()
print("Age:", my_dict.get("age"))

# 2. keys()
print("Keys:", my_dict.keys())

# 3. values()
print("Values:", my_dict.values())

# 4. items()
print("Items:", my_dict.items())

# 5. pop()
removed_item = my_dict.pop("weight")
print("After pop:", my_dict)

# 6. update()
my_dict.update({"hobby": "Gaming"})
print("After update:", my_dict)

# 7. clear() (creating a copy to demonstrate, as clear() empties the dictionary)
copy_dict = my_dict.copy()
copy_dict.clear()
print("After clear:", copy_dict)

# 8. copy()
new_dict = my_dict.copy()
print("Copied Dictionary:", new_dict)

# 9. setdefault()
default_value = my_dict.setdefault("gender", "Male")
print("After setdefault:", my_dict)

# 10. fromkeys()
new_keys = ["brand", "model", "year"]
new_dict_from_keys = dict.fromkeys(new_keys, "Unknown")
print("Dictionary from keys:", new_dict_from_keys)