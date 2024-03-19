low=int(input('enter lower:'))
up=int(input('enter upper:'))
even_sum=0
odd_sum=0
while(low<=up):
    if(low%2==0):
        even_sum+=low
    else:
        odd_sum+=low
    low+=1
print(even_sum)
print(odd_sum)
