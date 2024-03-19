def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return "elemnt found",mid
        elif(arr[mid]<target):
            low=mid+1
        else:
            high=mid-1
arr=[1,4,6,2,7,9,0]
r=binarysearch(arr,0)
print(r)


# def binarysearch(lst,n):
#     low=0
#     upper=len(lst)-1
#     while(low<=upper):
#         mid=(low+upper)//2
#         if(lst[mid]==n):
#             return 'element found', mid
#         elif(lst[mid]<n):
#             low=mid+1
#         else:
#             upper=mid-1
# lst=[1,2,13,4,5,3,55,0]
# n=5
# print(binarysearch(lst,n))
