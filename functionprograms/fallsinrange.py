# 6. Write a Python function to check whether a number falls within a given range.

def fall(n,k):
    for i in range(0,k):
        flag=0
        if(n<=k):
            flag=1
        else:
            flag=0
    if(flag==1):
        print('elements falls in the range')
    else:
        print('element execeds the range')
fall(203,90)

