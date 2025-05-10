
"""
Description: A list is a dynamic array that allows you to store a sequence of elements. It supports indexing, slicing, and various methods for manipulating the data.

Time Complexity:
Read: O(1) - Accessing an element by an index is fast and takes constant time.
Write: O(1) - Appending an element is usually O(1), but inserting or removing can be O(n) due to shifting elements.

"""

my_list = [1, 2, 3, 4, 5]

element = my_list[2] # O(1)
print(element)

my_list.append(6) # O(1)
print(my_list)

# Removing an element
my_list.remove(3)  # my_list = [1, 2, 4, 5, 6]
print(my_list)

# sort list in place
my_list.sort()
print(my_list)

# sort list in place in reverse order
my_list.sort(reverse=True)
print(my_list)

for idx, elt in enumerate(my_list):
    print(f'Use enumerate to get index: {idx} and element: {elt}')

for elt in my_list:
    print(f'Use loop directly to loop through elements: {elt}')