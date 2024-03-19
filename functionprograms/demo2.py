# def binary_search_least_positive_index(lst, target):
#     low, high = 0, len(lst) - 1
#     least_positive_index = -1
#
#     while low <= high:
#         mid = (low + high) // 2
#         mid_value = lst[mid]
#
#         if mid_value == target:
#             # Update the least positive index and continue searching in the left half
#             least_positive_index = mid
#             high = mid - 1
#         elif mid_value < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return least_positive_index
#
# # Example usage:
# numbers_list = [1, 5, 2, 4, 2, 50, 15, 7, 8, 9]
# target_element = 2
#
# # Find the least positive index of the target element using binary search
# result_index = binary_search_least_positive_index(numbers_list, target_element)
#
# # Print the result
# if result_index != -1:
#     print(f"The least positive index of {target_element} in the sorted list is: {result_index}")
# else:
#     print(f"{target_element} not found in the sorted list.")


def least_positive_integer(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > mid + 1:
            right = mid - 1
        else:
            left = mid + 1
    return left + 1

# Example usage:
sorted_array = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
result = least_positive_integer(sorted_array)
print("The least positive integer in the sorted array is:", result)