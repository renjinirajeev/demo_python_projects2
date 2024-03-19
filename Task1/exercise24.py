def WordCount(word):
    dic={}
    data=word.split(' ')
    for i in data:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic
    # for k,v in dic.items():
    #     return k,v
result=WordCount('Create a program that counts the number of words in a sentence')
print(result)

