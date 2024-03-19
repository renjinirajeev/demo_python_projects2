# def binarysearch(lst):
#     lst.sort()
#     lst1=[]
#     n=0
#     for i in lst:
#         if(i>0):
#             lst1.append(i)
#             break
#     # print(lst1)
#     for i in lst1:
#         n=i
#     print(n)
#     lst.sort()
#     k=len(lst)
#     lower = 0
#     upper=k-1
#     flag=0
#     k=0
#     for i in lst:
#         mid=lower+upper//2
#         if (n<lst[mid]):
#             upper=mid-1
#         elif(n>lst[mid]):
#             lower=mid+1
#         else:
#             # k = lst.index(i)
#             k=mid
#             flag=1
#     if(flag==1):
#         print('element found in the index',k)
#     else:
#         print('element not found')
#     print(lst)
# binarysearch([11,-3,6,3,-4,5,-31,-2,0,4,])

# def search(lst):
#     lst.sort()
#     print(lst)
#     n=0
#     lst1=[]
#     for i in lst:
#         if(i>0):
#             lst1.append(i)
#     n=lst1[0]
#     # k = len(lst)
#     lower=0
#     upper=len(lst)-1
#     k=0
#     flag=0
#     for i in lst:
#         mid=(upper+lower)//2
#         if(lst[mid]>n):
#             upper=mid-1
#         elif(lst[mid]<n):
#             lower=mid+1
#         else:
#             k=mid
#             flag=1
#     if(flag==1):
#         print('lowest postive integer',n,' found in index',k)
#     else:
#         print('element not found')
#
# search([11,-3,6,-3,-4,5,-31,-2,0,4,])



def search(lst):
    lst.sort()
    lst1=[]
    n=0
    for i in lst:
        if(i>0):
            lst1.append(i)
    n=lst1[0]
    # print(n)
    low=0
    high=len(lst)-1
    k=0
    flag=0
    for i in lst:
        mid=(low+high)//2
        if(lst[mid]<n):
            low=mid+1
        elif(lst[mid]>n):
            high=mid-1
        else:
            k=mid
            flag=1
    if(flag==1):
        print(n,'found in list',k)
    else:
        print(n,'not found in list')
lst=[11,-3,6,-3,-4,5,-31,-2,0,4,22]
search(lst)