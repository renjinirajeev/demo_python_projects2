string=input('Enter a string:')
vowels='AEIOUaeiou'
count=0
for i in string:
    if i in vowels:
        count+=1
print('No of vowels is :',count)