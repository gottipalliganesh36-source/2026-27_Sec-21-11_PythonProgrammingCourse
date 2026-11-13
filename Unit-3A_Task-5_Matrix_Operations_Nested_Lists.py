list_data = [1, 2, 2, 3, 1, 4, 3]
unique =[]

for items in list_data:  # each item in list_data
    if items:  # item not already in unique
        unique.append(items)  # append item

print("Original:", items)
print("Without duplicates:", items)