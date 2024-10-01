# Set is a collection of unique elements. It is enclosed within curly brackets. It is unordered, unindexed, mutable, and cannot contain duplicate elements

# Program to create an empty set
# s = {} - completely wrong as it is not a set it is a dictionary
s = set()  # correct way to make an empty set
s.add(1)
s.add(2)
s.add(3)
s.add(2)
s.add(2)
print(s)  # will give only 1, 2, 3 automatically removes duplicate elements

'''Very very important question for interview purpose
Is set a mutable or immutable data type?
So, set is mutable as we have seen above we are able to add elements in an empty set
and elements of set are immutable'''

# Let's discuss some of the functions of set
# pop() - will remove any random element from set
s.pop()
print(s)

# remove() - it will remove the element of your choice
s.remove(2)
print(s)

# clear() - will empty the set
s.clear()
print(s)

s1 = {5, 6, 7, 8, 9}
# union() - will combine elements of two sets
print(s1.union({2, 3}))

# intersection() - will take common elements of two sets
print(s1.intersection({3, 5}))

# Mistakes and Refactoring:
# 1. Fixed incorrect comments and grammar.
# 2. Improved readability and consistency in comments.