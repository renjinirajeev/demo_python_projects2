# Write a Python function to check whether a number is "Perfect" or not.

def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if (sum==n):
        return 'It is a perfect number'
    else:
        return 'It is not'
print(perfect(28))


# # first n perfect number
# def perfect(n):
#     sum=0
#     for i in range(1,n):
#         if (n%i==0):
#             sum+=1
#             if(sum==n):
#                 print(n)
# print(perfect())



