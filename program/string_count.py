# string='my name is renjini rs'
# count=0
# for i in string:
#     count+=1
# print(count)

# constraints count
string='my name is renjini rs'
count=0
vowels='aeiouAEIOU'
for i in string:
    if i not in vowels:
        count+=1
print(count)


# vowels count
string='my name is renjini rs'
count=0
vowels='aeiouAEIOU'
for i in string:
    if i in vowels:
        count+=1
print(count)


# space count
string='my name is renjini rs'
count=0
space=' '
for i in string:
    if i  in space:
        count+=1
print(count)