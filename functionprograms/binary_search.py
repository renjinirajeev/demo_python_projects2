# def binarysearch(lst):
#     num=int(input('enter a number:'))
#     low=0
#     upper=len(lst)-1
#     k = lst.index(num)
#     lst.sort()
#     flag=0
#     for i in lst:
#         mid=(low+upper)//2
#         if(num<lst[mid]):
#             upper=mid-1
#         elif(num>lst[mid]):
#             low=mid+1
#         else:
#             flag=1
#
#     if(flag==1):
#         print('element found',k)
#     else:
#         print('element not found')
#     print(lst)
# binarysearch([1,4,2,6,21,6,2,8,2,9,2,9,3,9,1])


def binarysearch(lst,n):
    lst.sort()
    k=len(lst)
    low=0
    upper=len(lst)-1
    flag=0
    k=0
    for i in lst:
        mid=(low+upper)//2
        if(lst[mid]<n):
            low=mid+1
        elif(lst[mid]>n):
            upper=mid-1
        else:
            k=mid
            flag=1
    if(flag==1):
        print(n,"element found in the list",k)
    else:
        print(n,'element not found in the list')
lst=[1,3,524,25,2,6,22,76,45]
n=524
binarysearch(lst,n)