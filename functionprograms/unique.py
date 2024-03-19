# a=[1,2,3,4,3,2,1]
# count=0
# dic={}
# for i in a:
#     if i not in dic:
#         dic[i]=1
#     else:
#         count+=1
# for k,v in dic.items():
#     if(a[v]==1):
#         print(k)

# def find_single_occurrence_elements(input_list):
    # element_count = {}
    #
    # # Count occurrences of each element in the list
    # for element in input_list:
    #     if element in element_count:
    #         element_count[element] += 1
    #     else:
    #         element_count[element] = 1
    #
    # # Filter elements with only one occurrence
    # single_occurrence_elements = [key for key, value in element_count.items() if value == 1]
    #
    # return single_occurrence_elements


# Example usage:
# my_list = [1, 2, 3, 4, 1, 2, 5, 6, 3, 5]
# result = find_single_occurrence_elements(my_list)
# print("Elements occurring only once:", result)

lst= [1, 2, 3, 4, 1, 2, 5, 6, 3, 5]
# count=0
# dic={}
# for i in lst:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# for k,v in dic.items():
#     if(v==1):
#         print(k)

#
# def lonelyinteger(a):
#     # Write your code here
#     result = 0
#     for i in a:
#         result ^= i
#     return result
# print(lonelyinteger([1, 2, 3, 4, 3, 2,1 ]))


# def find_single_occurrence_elements(lst):
#     element_count = {}
#
#     # Count occurrences of each element in the list
#     for element in lst:
#         if element in element_count:
#             element_count[element] += 1
#         else:
#             element_count[element] = 1
#
#     # Print elements that occur only once
#     print("Elements that occur only once:")
#     for element, count in element_count.items():
#         if count == 1:
#             print(element)
#
#
# # Example usage:
# my_list = [1, 2, 3, 4, 2, 1, 5, 6, 7, 7, 8]
# find_single_occurrence_elements(my_list)

def unique(lst):
    dic={}
    for i in lst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for k,v in dic.items():
        if v==1:
            print(k)
lst=[1,2,3,3,2,4,6,7,5,5]
unique(lst)
