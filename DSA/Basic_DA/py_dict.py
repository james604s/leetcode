"""
Description: A dictionary is an unordered collection of key-value pairs. It allows for fast lookups, insertions, and deletions based on keys.

Time Complexity:

Read: O(1) - Accessing a value by key is fast due to the underlying hash table.
Write: O(1) - Inserting or deleting a key-value pair is also fast, thanks to the hash table.
"""

my_dict = { 'a': 1, 'b': 2, 'c': 3 }
value = my_dict['a']
print(value)

# Adding a key-value pair
my_dict['d'] = 4  # my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict)

# Removing a key-value pair
del my_dict['a']  # my_dict = {'b': 2, 'c': 3, 'd': 4}
print(my_dict)
