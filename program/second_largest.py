num1=int(input('enter number1:'))
num2=int(input('enter number2:'))
num3=int(input('enter number3:'))


if(num1>num2) & (num1>num3):
    if(num2>num3):
        print(num2,'is second largest')
    else:
        print(num3,'is second largest')
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print(num1,'is second largest')
    else:
        print(num3,'is second largest')
elif(num3>num1)&(num3>num1):
    if(num1>num2):
        print(num1,'is second largest')
    else:
        print(num2,'is second largest')
else:
    print("invalid")