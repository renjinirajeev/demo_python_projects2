# 1.	Write a Python program to print "Hello, World!" to the screen.
print("Hello, World!" )

# 2.	Write a program to take user input (their name) and display it on the screen.
name=input('Enter Youe Name:')
print('My name is',name)

# 3.	Create a Python program to calculate the sum of two numbers.
a=int(input('Enter number 1:'))
b=int(input('Enter number 2:'))
sum=a+b
print('Sum is:',sum)

# 4.	Write a program to check if a number is even or odd.
a=int(input('enter a number:'))
if(a%2==0):
    print(a,'is even')
else:
    print(a,'is odd')

# 5.	Create a program that calculates the square of a number.
num=int(input('enter a number:'))
squ=num**2
print('square of',num,'is:',squ)

# 6.	Write a Python program to find the maximum of two numbers.
num1=int(input('enter number 1:'))
num2=int(input('enter number 2:'))
if(num1>num2):
    print(num1,'is greater than',num2)
elif(num1<num2):
    print(num2,'is greater than',num1)
else:
    print(num1,'is equal to',num2)

# 7.	Write a program that prints the numbers from 1 to 10.
for i in range(1,11):
    print(i)

# 8.	Create a Python program to print the multiplication table of a given number.
n=int(input('enter a number:'))
for i in range(1,11):
    j=n*i
    print(i,'*',n,'=',j)

# 9.	Write a program to check if a given number is positive, negative, or zero.
n=int(input('enter a number:'))
if(n>0):
    print(n,'is positive')
elif(n<0):
    print(n,'is negative')
else:
    print(n, 'is zero')

# 10.	Create a program that calculates the factorial of a number.
n=int(input('Enter a number:'))
fact=1
for i in range(1,n+1):
    fact*=i
print('Factorial of',n,'is',fact)


# 11.	Write a Python program to check if a number is prime.
n=int(input('Enter a number:'))
flag=0
if(n<=1):
    print(n,'is not prime')
else:
    for i in range(2,n):
        if(n%i==0):
            flag=1
    if(flag==1):
        print(n,'is not prime')
    else:
        print(n,'is prime')

# 12.	Create a program to swap the values of two variables.
num1=int(input('enter number 1:'))
num2=int(input('enter number 2:'))
print('Before swapping')
print('Number 1:',num1)
print('Number 2:',num2)
num1,num2=num2,num1
print('After swapping')
print('Number 1:',num1)
print('Number 2:',num2)


# 13.	Write a program to calculate the average of a list of numbers.
lst=[2,4,1,5,7,8,9,3]
s=sum(lst)
length=len(lst)
average=s/length
print('Average is',average)

# 14.	Create a program that finds the largest number in a list.
lst=[2,4,1,5,7,8,9,3]
print('Largest number is:',max(lst))

# 15.	Write a Python program to reverse a string.
string=input('Enter a string:')
rev=string[::-1]
print('Reverse of the string is:',rev)

# 16.	Create a program to find the length of a string.
string=input('enter a string:')
count=0
for i in string:
    count+=1
print('length of the string is:',count)

# 17.	Write a program to check if a string is a palindrome.
string=input('enter a string:')
if(string[::]==string[::-1]):
    print(string,'is palindrome')
else:
    print(string,'is not palindrome')

# 18.	Create a program to count the number of vowels in a string.
string=input('Enter a string:')
vowels='AEIOUaeiou'
count=0
for i in string:
    if i in vowels:
        count+=1
print('No of vowels is :',count)

# 19.	Write a Python program to find the sum of all even numbers from 1 to 100.
sum=0
for i in range(1,101):
    if(i%2==0):
        sum+=i
print('Sum of even numbers from 1 to 100 is:',sum)

# 20.	Create a program to check if a given year is a leap year.
year=int(input('enter the year:'))
if(year%400==0 or year%100!=0 and year%4==0):
    print(year,'is a leap year')
else:
    print(year, 'is not a leap year')


# 21.	Write a program that generates a random number and asks the user to guess it.
import random
random=random.randint(1,100)
tries=0
num=0
while(num!=random):
    num=int(input('Guess a number (1 to 100) :'))
    tries+=1
    if(num<random):
        print('Too low, try again')
    elif(num>random):
        print('Too high, try again')
    else:
        print('Correct,you got in ',tries,'tries')


# 22.	Create a program that converts Fahrenheit to Celsius.
fahrenheit=float(input('enter the Fahrenheit :'))
celsius=(fahrenheit-32)*5/9
print('Fahrenheit value is:',fahrenheit)
print('Celsius value is:',celsius)

# 23.	Write a Python program to calculate the area of a rectangle.
def area(l,b):
    A=l*b
    print('Area of the rectangle is:',A)
area(2,5)

# 24.	Create a program that counts the number of words in a sentence.
def WordCount(word):
    dic={}
    data=word.split(' ')
    for i in data:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic
result=WordCount('Create a program that counts the number of words in a sentence')
print(result)


# 25.	Write a program to find the common elements between two lists.
lst1=[2,4,6,3,8,61]
lst2=[3,6,1,5,8,2]
for i  in lst1:
    if i in lst2:
        print(i)

# 26.	Create a program that sorts a list of numbers in ascending order.
lst=[44,76,21,53,32,10,7,49]
print('list is:',lst)
lst.sort()
print('sorted list is:',lst)

# 27.	Write a Python program to find the second largest element in a list.
lst=[44,76,21,53,32,10,7,49]
lst.sort(reverse=True)
print('Second largest element is',lst[1])

# 28.	Create a program that generates a simple calculator.
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



# 29.	Write a program to check if a given string contains only digits.
string=input('enter the string:')
number='1234567890'
flag=0
for i in string:
    if i in number:
        flag=1

if(flag==1):
    print('String contain digits')
else:
    print('String not contain digits' )

# 30.	Create a program to calculate the sum of all prime numbers from 1 to 100.
sum=0
for i in range(1,101):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            sum+=i
print('sum is:',sum)