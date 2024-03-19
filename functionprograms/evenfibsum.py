# def evenfibsum(n):
#     sum=0
#     a=0
#     b=1
#     while(b<n):
#         if(b%2==0):
#             sum+=b
#             h=a+b
#             a, b = b, h
# evenfibsum(10)

# def fib():
#     limit=int(input('enter a number:'))
#     sum = 0
#     a = 1
#     b = 1
#     while (b < limit):
#
#         if( b % 2 == 0):
#             sum += b
#         h = a + b
#         a, b = b, h
#     print(sum)
# fib()

def fib():
    n=int(input('n:'))
    sum=0
    a,b=0,1
    while(b<n):
        if(b%2==0):
            sum += b
        h = a + b
        a, b = b, h
    print(sum)
fib()




