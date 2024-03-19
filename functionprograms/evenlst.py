def evenlst(lst):
    elst=[]
    for i in lst:
        if(i%2==0):
            elst.append(i)
    return elst
print(evenlst([1,25,2,6,1,6,3,0,4,2,1,7,9]))
