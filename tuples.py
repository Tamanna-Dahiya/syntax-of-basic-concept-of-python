# Tuple is an immutable data type
# It is enclosed by round brackets
t = ([1, 2], 3)

# Indexing as same concepts as we discussed in strings and lists
print(t[0])
# t[0] = 1  # not possible to do this as tuple is immutable, it will throw type error

# WAP to create an empty tuple
t = ()

# To create a tuple of a single element
t = (1,)  # comma after this 1 is necessary if this is not given and if you fetch its type then it will come as integer
t = (2)
print(type(t))  # int

# Now let's discuss the methods of tuple
# index() - it will give you the index of the first occurrence of an element in the tuple if the element does not exist then value error will come
t1 = (1, 2, 3, 4, 3, 2)
print(t1.index(2))

# count() - it will tell how many times an element comes in the tuple if the element does not exist then it will give 0
print(t1.count(2))

# Mistakes and Refactoring:
# 1. Fixed incorrect method name (find() to index()).
# 2. Improved readability and consistency in comments.