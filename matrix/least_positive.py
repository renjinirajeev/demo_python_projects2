# def leastpositive(matrix):
#     pos_no=float('inf')
#     for i in matrix:
#         for j in i:
#             # print(j)
#             if (j>0 and j<pos_no):
#                 pos_no=j
#     if (pos_no == float('inf')):
#         print('No positive element')
#     else:
#         print('Least positive element is:',pos_no)
# matrix=[
#     [12,21,4,6],
#     [55,66,8,3],
#     [20,22,64,10]
# ]
#
#
#
# leastpositive(matrix)


# def leastpositive(matrix):
#     pos_no=float('inf')
#     for i in matrix:
#         for j in i:
#             if(j>0 and j<pos_no):
#                 pos_no=j
#     if(pos_no==float('inf')):
#         print("no positive element in matrix")
#     else:
#         print("least positive element is:",pos_no)
#
# matrix=[
#     [12,21,42,-6],
#     [55,66,8,39],
#     [20,22,64,10]
# ]
# leastpositive(matrix)


def least_pos(matrix):
    pos_no=float('inf')
    for i in matrix:
        for j in i:
            if(j>0 and j<pos_no):
                pos_no=j
    if(pos_no==float('inf')):
        print('no positive integer')
    else:
        print('least positive integer is:',pos_no)
matrix=[
    [12,21,42,-6],
    [55,66,8,39],
    [20,22,64,10]
]
least_pos(matrix)
