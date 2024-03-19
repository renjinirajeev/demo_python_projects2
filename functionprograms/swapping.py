# using third variable
str1='renjini'
str2='rajeev'
print("1st string:",str1)
print("2nd string:",str2)

temp=str1
str1=str2
str2=temp
print("1st string:",str1)
print("2nd string:",str2)

#-------------------------------------*-----------------------------------

#using single line

st1,st2='renji','renjini'
print("1st string:",st1)
print("2nd string:",st2)
st1,st2=st2,st1
print("1st string:",st1)
print("2nd string:",st2)

#-------------------------------------*-----------------------------------

#using arithemetic operation

num1=2
num2=4
print("no 1 is:",num1)
print("no 2 is:",num2)

num1=num1+num2   #num1=6
num2=num1-num2   #num2=6-4=2
num1=num1-num2   #num1=6-2=4
print("no 1 is:",num1)
print("no 2 is:",num2)




