sum=0
for i in range(1,101):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            sum+=i
print('sum is:',sum)