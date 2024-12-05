# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_list[0]
last_element = my_list[-1]

# Adding elements
my_list.append(6)

# Inserting an element at a specific position
my_list.insert(2, 10)

# Removing an element
my_list.remove(10)

# Popping the last element
popped_element = my_list.pop()

# Slicing the list
sliced_list = my_list[1:4]

# Finding the index of an element
index_of_3 = my_list.index(3)

# Checking if an element exists
exists = 3 in my_list

# Sorting the list
my_list.sort()

# Reversing the list
my_list.reverse()

# Combining two lists
another_list = [7, 8, 9]
combined_list = my_list + another_list

# List comprehension
squared_list = [x ** 2 for x in my_list]

print(f"First element: {first_element}")
print(f"Last element: {last_element}")
print(f"Popped element: {popped_element}")
print(f"Sliced list: {sliced_list}")
print(f"Index of 3: {index_of_3}")
print(f"Element exists: {exists}")
print(f"Sorted list: {my_list}")
print(f"Reversed list: {my_list}")
print(f"Combined list: {combined_list}")
print(f"Squared list: {squared_list}")
