
# def fizzBuzz(n):
#     # Write your code here
#     for i in range(1,n+1):
#         if(i%3==0):
#             print('Fizz')
#         elif(i%5==0):
#             print('Buzz')
#         elif(i%5==0)and (i%3==0):
#             print('FizzBuzz')
#         else:
#             print(i)
# fizzBuzz(15)

# n=8
# lst=[1,3,5,0,6,8,2,9]   #[0,1,2,3,5,6,8,9]
# lst.sort()
# # print(lst[n//2])    #median for odd number
# # print((lst[n//2]+lst[n//2+1])/2)
# median=len(lst)//2
# print(lst[median])

# def find_median(even_list):
#     sorted_list = sorted(even_list)
#     mid = len(sorted_list) // 2
#     return (sorted_list[mid - 1] + sorted_list[mid]) / 2
#
# # Example usage:
# even_list = [3, 7, 2, 9, 5, 8]
# median = find_median(even_list)
# print("Median of the list:", median)


def find_median(even_list):
    sorted_list=sorted(even_list)
    mid=len(sorted_list)//2
    if(mid%2==1):
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
even_list=[3,7,2,9,5,0]
median=find_median(even_list)
print(median)