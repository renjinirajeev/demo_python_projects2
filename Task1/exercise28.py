def add(num1,num2):
    result=num1+num2
    return result

def sub(num1,num2):
    result=num1-num2
    return result

def mul(num1,num2):
    result=num1*num2
    return result

def div(num1,num2):
    if(num2!=0):
        result=num1/num2
        return result
    else:
        return 'cannot divided by zero'

num1=int(input('enter number1:'))
num2=int(input('enter number2:'))
operation=input('enter the operation(+,-,*,/):')

if(operation=='+'):
    print(num1,'+',num2,'=',add(num1,num2))
if(operation=='-'):
    print(num1,'-',num2,'=',sub(num1,num2))
if(operation=='*'):
    print(num1,"*",num2,'=',mul(num1,num2))
if(operation=='/'):
    print(num1,'/',num2,'=',div(num1,num2))


