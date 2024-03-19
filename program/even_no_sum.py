lower=int(input('lower:'))
upper=int(input('upper:'))
sum=0
while(lower<=upper):
    if(lower%2==0):
        sum+=lower
    lower+=1
print(sum)