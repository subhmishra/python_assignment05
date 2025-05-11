                                    #Task 2: Demonstrate List Slicing

numbers = list(range(1, 11))
print("original list :",numbers)

extracted_list = numbers[:5]

reversed_list = extracted_list[::-1]

print("Extracted first five elements:", extracted_list)
print("Reversed extracted elements:", reversed_list)


#output
# original list : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Extracted first five elements: [1, 2, 3, 4, 5]
# Reversed extracted elements: [5, 4, 3, 2, 1]