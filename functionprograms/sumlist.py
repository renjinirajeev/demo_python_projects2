# def add():
#     lst=[1,6,3,8,3,8,2,9,2,9,10]
#     print(sum(lst))
# add()

def multiply(lst):

    mul=1
    for i in lst:
        mul *= i
    return mul

print(multiply( [1, 6, 3, 8, 3, 8, 2, 9, 2, 9, 10]))