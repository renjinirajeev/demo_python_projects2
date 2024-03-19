# def noofstep(n):
#     step=0
#     k=0
#     while(n!=1):
#         if(n%5==0):
#            k=n/5
#         elif(n%3==0):
#             k=n/3
#         else:
#             k=n/2
#         step+=1
#     print(step)
# # noofstep(24)
#
# n=int(input('enter a number:'))
# step=0
# k=0
# for i in range(0,n):
#     if(n%5==0):
#         k=n/5
#     elif(n%3==0):
#         k=n/3
#     else:
#         k=n/2
#     step+=1
# print(step)



def find_step(N):
    step=0
    while(N!=1):
        if(N%5==0):
            N=N/5
            step+=1
        elif(N%3==0):
            N=N/3
            step+=1
        else:
            N=N/2
            step+=1
    return step
input_numb=int(input('enter the number:'))
step=find_step(input_numb)
print(step)

