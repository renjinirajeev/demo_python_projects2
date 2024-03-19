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
