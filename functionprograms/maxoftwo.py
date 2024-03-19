def maxNumber(x,y,z):
    if(x>y)&(x>z):
        print(x,'x is largest')
    elif(x<y)&(y>z):
        print(y,'y is largest')
    else:
        print(z,'z is largest')

maxNumber(10,2,5)