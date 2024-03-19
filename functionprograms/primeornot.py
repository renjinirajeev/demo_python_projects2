# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def prime():
    num=int(input('enter a number:'))
    flag=0
    if(num<=1):
        print('It is not prime ')
    # elif(num<=0):
    #     print('It is not prime')
    else:
        for i in range(2,num):
            if(num%i==0):
                flag=1
        if(flag>0):
            print('It is not prime')
        else:
            print('it is prime')
prime()

# def prime():
#     num = int(input("Enter a number:"))
#     flag = 0
#     if (num == 1):
#         print("Number is neither prime nor not")
#     elif (num <= 0):
#         print("Not a prime")
#     else:
#         for i in range(2, num):
#             if (num % i == 0):
#                 flag = 1
#         if (flag > 0):
#             print("not a prime")
#         else:
#             print("Number is prime")
# prime()