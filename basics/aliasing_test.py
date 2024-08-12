import copy

# Create an original list
original_list = [1, 2, [3, 4]]

# Create an alias for the original list
alias_list = original_list

# Create a shallow copy of the list
shallow_copy = original_list.copy()

# Create a deep copy of the list
deep_copy = copy.deepcopy(original_list)

# Modify the alias list
alias_list.append(5)

# Modify an element inside the nested list via alias
alias_list[2][0] = 9

# Assign a new list to the alias
alias_list = [6, 7, 8]

# Print all lists to see the effects of modifications
print("Original list after alias modifications:", original_list)  # Output: [1, 2, [9, 4], 5]
print("Alias list after new assignment:", alias_list)            # Output: [6, 7, 8]
print("Shallow copy after original list modification:", shallow_copy)  # Output: [1, 2, [9, 4]]
print("Deep copy after original list modification:", deep_copy)        # Output: [1, 2, [3, 4]]

# Modify the nested list in the original list
original_list[2][1] = 10

# Print all lists to see the effects of further modifications

print("Original list after further modification:", original_list)  # Output: [1, 2, [9, 10], 5]
print("Shallow copy after further original list modification:", shallow_copy)  # Output: [1, 2, [9, 10]]
print("Deep copy remains unchanged:", deep_copy)                   # Output: [1, 2, [3, 4]]
