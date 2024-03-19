# def search(arr,target):
#     iteration=0
#     for i in arr:
#         iteration+=1
#         if(i==target):
#             print('number found at index:',i)
#             return iteration
#     print('number not found in list')
#     return iteration
# lst=[3,4,1,4,7,9,2,5,6]
# target=7
# iteration=search(lst,target)
# print('number of iteration:',iteration)


# def search(lst,num):
#     iteration=0
#     for i in lst:
#         iteration+=1
#         if(i==num):
#             print('number found at index:')
#             return iteration
#     print('number not found in list')
#     return iteration
# lst=[3,29,1,8,40,32,7,89,4]
# num=32
# iteration=search(lst,num)
# print(iteration)


# def search(lst,n):
#     iteration=0
#     k=0
#     num=0
#     for i in lst:
#         iteration+=1
#         if(i==num):
#             k=lst.index(i)
#             print('number found at index',k)
#             # print(iteration)
#         else:
#             print('number not found')
#     print(iteration)
# search([3,29,1,8,40,32,7,89,4],40)

num=int(input('no:'))
lst=[3,29,1,8,40,32,7,89,4]
# k=0
for i in lst:
    if(num==i):
        flag=1
        k=lst.index(i)
        # print('element found in index')
        # print('not found')
if(flag==1):
    print('element found in index',k)
else:
    print('element not in index')

