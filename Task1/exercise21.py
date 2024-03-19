import random
random=random.randint(1,100)
tries=0
num=0
while(num!=random):
    num=int(input('Guess a number (1 to 100) :'))
    tries+=1
    if(num<random):
        print('Too low, try again')
    elif(num>random):
        print('Too high, try again')
    else:
        print('Correct,you got in ',tries,'tries')

