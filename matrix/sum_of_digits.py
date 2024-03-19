

def digit_sum(n):
    digitsum=0
    while(n>=10):
        digitsum=sum(int(i) for i in str(n))
        n=digitsum
    print(digitsum)
digit_sum(9875)


