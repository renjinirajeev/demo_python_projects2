#current year

#current month

#current date

#birth year

#birth month

#birth date

#print age

#2023
#11
#24

#2022 11 25 =0

current_year=int(input("enter current year:"))
current_month=int(input("enter current month:"))
current_date=int(input("enter current date:"))
birth_year=int(input("enter birth year:"))
birth_month=int(input("enter birth month:"))
birth_date=int(input("enter birth date:"))
age=current_year-birth_year
month=current_month-birth_month
day=current_date-birth_date

if(age>0):
    if(month>0):
        print(age)
    elif(month==0) and (day>=0):
        print(age)
    elif(month==0) and (day<0):
        print(age-1)
    else:
        print(age-1)
elif(age==0):
    if(month>0):
        print(age)
    elif(month==0) and(day>=0):
        print(age)
    elif(month==0) and(day<0):
        print('inavlid')
    else:
        print('invalid')
else:
    print('invalid')
