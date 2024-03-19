# def paranthesis(lst):
#     stack=[]
#     ex_par=[]
#     n=len(lst)
#     res=[]
#     for i in range(n):
#         if(lst[i]=="("):
#             stack.append(i)
#         elif(lst[i]==")"):
#             if stack:
#                 stack.pop()
#             else:
#                 ex_par.append(i)
#     ex_par.extend(stack)
#
#     result_list = [lst[i] for i in range(n) if i not in ex_par]
#
#     result = "".join(result_list)
#     return result
#
#
#
# data=list("'hai renji(i am ) ranjeev(('))))((")
# print(paranthesis(data))



# def paranthesis(lst):
#     stack=[]
#     ex_par=[]
#     n=len(lst)
#     for i in range(n):
#         if(lst[i]=="("):
#             stack.append(i)
#         elif(lst[i]==")"):
#             if stack:
#                 stack.pop()
#             else:
#                 ex_par.append(i)
#     ex_par.extend(stack)
#     result_lst=[lst[i] for i in range(n) if i not in ex_par]
#     result="".join(result_lst)
#     return result
# data=list("hai renji(i am ) ranjeev(('))))(((")
# print(paranthesis(data))


def paranthesis(lst):
    stack=[]
    ex_par=[]
    for i in range(len(lst)):
        if(lst[i]=="("):
            stack.append(i)
        elif(lst[i]==")"):
           if stack:
               stack.pop()
           else:
               ex_par.append(i)
    ex_par.extend(stack)
    result_lst=[lst[i] for i in range(len(lst)) if i not in ex_par]
    result="".join(result_lst)
    print(result)
paranthesis("hai renji(i am ) ranjeev(('))))(((")




