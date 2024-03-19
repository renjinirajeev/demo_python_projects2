# #unit
# 100 no charge
# 101-200     1unit=5rs
# above 200   1 unit = 10 rs
# calculate electricity bill

unit=int(input('enter no of units'))

c1=(unit-100)*5
c2=(unit-200)*10+500

if(unit<=100):
    print('no charge')
elif(101<=unit<=200):
    print('charges is c1',c1)
else:
    print('charge is c2',c2)