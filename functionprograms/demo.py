# def binary_search(input_list, target):
#     low, high = 0, len(input_list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         mid_value = input_list[mid]
#
#         if mid_value == target:
#             return mid  # Element found, return its index
#         elif mid_value < target:
#             low = mid + 1  # Discard the left half
#         else:
#             high = mid - 1  # Discard the right half
#
#     return -1  # Element not found
#
# # Example usage:
# sorted_numbers = [1, 2, 6, 4, 7, 5, 3, 8, 9]
# target_element = 6
#
# # Find the index of the target element using binary search
# result_index = binary_search(sorted_numbers, target_element)
#
# # Print the result
# if result_index != -1:
#     print(f"The index of {target_element} in the sorted list is: {result_index}")
# else:
#     print(f"{target_element} not found in the sorted list.")



def find_lowest_positive_integer(lst):
    lowest_positive = None
    index = -1

    for i, num in enumerate(lst):
        if num > 0 and (lowest_positive is None or num < lowest_positive):
            lowest_positive = num
            index = i

    return lowest_positive, index

# Example usage:
numbers_list = [3, -1, 7, 0, 10, 2, 4, -2]
result_element, result_index = find_lowest_positive_integer(numbers_list)

# Print the result
if result_element is not None:
    print(f"The lowest positive integer is {result_element} at index {result_index}.")
else:
    print("No positive integers found in the list.")



# def binary_search_lowest_positive(lst):
#     low, high = 0, len(lst) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         mid_value = lst[mid]
#
#         if mid_value == mid + 1:
#             # The current element is in the correct position, search in the right half
#             low = mid + 1
#         elif mid_value > mid + 1:
#             # The lowest positive integer is in the left half
#             high = mid - 1
#         else:
#             # The lowest positive integer is in the right half
#             low = mid + 1
#
#     # The final value of 'low' is the index of the lowest positive integer
#     return lst[low], low
#
# # Example usage:
# numbers_list = [3, -1, 7, 0, 1, 2, 4, -2]
# lowest_positive, index_of_lowest_positive = binary_search_lowest_positive(sorted(numbers_list))
#
# # Print the result
# if index_of_lowest_positive != -1:
#     print(f"The lowest positive integer in the list is {lowest_positive} at index {index_of_lowest_positive}.")
# else:
#     print("No positive integer found in the list.")
#
