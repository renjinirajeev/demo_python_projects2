def UpperLower(string):
    up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upcount=0
    lowcount=0
    for i in string:
        if i not in up:
            lowcount+=1
        else:
            upcount+=1
    print('UPPER COUNT:',upcount)
    print('LOWER COUNT:',lowcount)
UpperLower('MynamEISrENjiNIrS')