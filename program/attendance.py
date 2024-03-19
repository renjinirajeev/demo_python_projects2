no_of_cls=int(input("enter total no of cls:"))
no_of_cls_attend=int(input("enter no of cls attended:"))
percentage=(no_of_cls_attend/no_of_cls)*100
print(percentage)
if(percentage>=75):
    print('student can attend exam')
else:
    print('cannot attend the exam')