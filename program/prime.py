# low=int(input('low:'))
# up=int(input('up:'))
# for i in range(low,up+1):
#     if(i>1):
#         for j in range(2,i):
#           if(i%j==0):
#               break
#         else:
#             print(i)


n=int(input('enter a number:'))
flag=0
if(n==1):
    print('Not a prime')
elif(n<=0):
    print('not a prime')
else:
    for i in range(2, n):
        if (n % i == 0):
            flag = 1
    if (flag == 0):
        print('is prime')
    else:
        print('not prime')
