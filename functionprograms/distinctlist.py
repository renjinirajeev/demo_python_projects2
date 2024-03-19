# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# def distinctlst():
#     lst=[1, 3, 6, 2, 6, 2, 2, 4, 8, 3, 7, 3, 7, 9, 2, 1, 0]
#     lst1=[]
#     for i in lst:
#         if i in lst1:
#             lst1.append(i)
#     print(lst1)
# distinctlst()

# lst=[1, 3, 6, 2, 6, 2, 2, 4, 8, 3, 7, 3, 7, 9, 2, 1, 0]
# lst1=[]
# for i in lst:
#     # if i not in lst1:
#     #     lst1.append
#    print(lst1)

# lst=[1, 3, 6, 2, 6, 2, 2, 4, 8, 3, 7, 3, 7, 9, 2, 1, 0]
# lst1=[]
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)


def distinct(lst):
    lst1=[]
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    print(lst1)
distinct([1, 3, 6, 2, 6, 2, 2, 4, 8, 3, 7, 3, 7, 9, 2, 1, 0])