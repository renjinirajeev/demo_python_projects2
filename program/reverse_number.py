num=int(input('enter a number:'))
rev=0
while(num>0):      #123
    temp=num%10    #12       3
    rev=rev*10+temp   #3
    num=num//10          #123//10=12   123/10=12   rem :  3
print(rev)
