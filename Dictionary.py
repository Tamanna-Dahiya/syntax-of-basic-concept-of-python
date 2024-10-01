# Dictionary is a datatype that stores key-value pairs. It is stored in curly brackets {}
'''Dictionary is mutable, unordered, indexed but can't contain duplicate keys'''
d = {"name": "tamanna", "course": "btechcse", "year": 1}  # if you give duplicate keys in a dictionary then you will get a name error

# To access values by using keys
print(d["name"])  # if you commit some error in the name of keys then you will get a key error

# To create an empty dictionary
d = {}

# To add keys in an empty dictionary
d["name"] = "Tamanna Dahiya"
d["profession"] = "student"
print(d)

# Nested dictionary - in simple words nested dictionary means a dictionary within another dictionary
d1 = {"a": {"b": 2}, "d": 3}

# You can also give list or tuple as a value in a dictionary
# One most important point - in a dictionary two values can be the same but two keys cannot

# Now let's discuss some of the most important methods of dictionary
# .keys() - it will give you all the keys present in a dictionary (keys will be given in a list)
print(d.keys())

# .values() - it will give you all the values of the dictionary (values will be given in a list)
print(d.values())

# .items() - it will give a combination of key and value pair in a tuple
print(d.items())

# .get() - its work will be similar to this (print(d["name"]))
# but the benefit of using .get is if you give the wrong name of the key then it will give None
print(d.get("name"))

# .update() - it will update the dictionary with the given key-value pair
d.update({"me": "learner"})
print(d)

# Mistakes and Refactoring:
# 1. Fixed indentation and spacing issues.
# 2. Corrected comments for better readability.
# 3. Removed unnecessary comments and improved grammar.
