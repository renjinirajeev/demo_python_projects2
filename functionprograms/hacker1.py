def plusMinus(arr):
    # Write your code here\
    n=len(arr)
    count=0
    for i in arr:
        if(i>0):
            count+=1
            return count/n
        elif(i<0):
            count+=1
            return count/n
        else:
            count+=1
            return count/n
        # return count/n
print(plusMinus([-4,-3,-6,0,2,3]))
