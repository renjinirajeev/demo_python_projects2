# # Python program to demonstrate
# # symmetry and palindrome of the
# # string
#
#
# # Function to check whether the
# # string is palindrome or not
# def palindrome(a):
#     # finding the mid, start
#     # and last index of the string
#     mid = (len(a) - 1) // 2  # you can remove the -1 or you add <= sign in line 21
#     start = 0  # so that you can compare the middle elements also.
#     last = len(a) - 1
#     flag = 0
#
#     # A loop till the mid of the
#     # string
#     while (start <= mid):
#
#         # comparing letters from right
#         # from the letters from left
#         if (a[start] == a[last]):
#
#             start += 1
#             last -= 1
#
#         else:
#             flag = 1
#             break;
#
#     # Checking the flag variable to
#     # check if the string is palindrome
#     # or not
#     if flag == 0:
#         print("The entered string is palindrome")
#     else:
#         print("The entered string is not palindrome")
#
#
# # Function to check whether the
# # string is symmetrical or not
# def symmetry(a):
#     n = len(a)
#     flag = 0
#
#     # Check if the string's length
#     # is odd or even
#     if n % 2:
#         mid = n // 2 + 1
#     else:
#         mid = n // 2
#
#     start1 = 0
#     start2 = mid
#
#     while (start1 < mid and start2 < n):
#
#         if (a[start1] == a[start2]):
#             start1 = start1 + 1
#             start2 = start2 + 1
#         else:
#             flag = 1
#             break
#
#     # Checking the flag variable to
#     # check if the string is symmetrical
#     # or not
#     if flag == 0:
#         print("The entered string is symmetrical")
#     else:
#         print("The entered string is not symmetrical")
#
#
# # Driver code
# string = 'amaama'
# palindrome(string)
# symmetry(string)
#
#
# # symmetric: khokho  --  kho   kho
# # palindrome: madam --   m a d a m


def palindrome(n):
    if (n[::]==n[::-1]):
        print('It is a palindrome')
    else:
        print('It is not a palindrome')
palindrome('madam')

# def palindrome(a):
#     n=len(a)
#     mid=n//2
#     first=0
#     last=n-1
#     flag=0
#     while(first<=mid):
#         if(a[first]==a[last]):
#             first+=1
#             last-=1
#         else:
#             flag=1
#             break
#     if(flag==0):
#         print('it is palindrome')
#     else:
#         print('it is not palindrome')
# def symmertic(a):
#     n=len(a)
#     flag=0
#     if(n%2):
#         mid=n//2+1
#     else:
#         mid=n//2
#     start1=0
#     start2=mid
#     while(start1<mid and start2<n):
#         if(a[start1]==a[start2]):
#             start1=start1+1
#             start2=start2+1
#         else:
#             flag=1
#             break
#     if(flag==0):
#         print('It is symmetric')
#     else:
#         print('It is not symmetric')
# string='khokho'
# palindrome(string)
# symmertic(string)




def palindrome(a):
    n=len(a)
    start=0
    end=n-1
    mid=(start+end)//2
    flag=0
    while(start<mid):
        if(a[start]==a[end]):
            start+=1
            end-=1
        else:
            flag=1
            break
    if(flag==1):
        print('its is not palindrome')
    else:
        print('it is palindrome')
def symmetric(a):
    n=len(a)
    start=0
    end=n-1
    if(n%2):
        mid=(start+end)//2+1
    else:
        mid=(start+end)//2
    start1=0
    start2=mid
    flag=0
    while(start1<mid and start2<n):
        if(a[start1]==a[start2]):
            start1+=1
            start2+=1
        else:
            flag=1
            break
    if(flag==1):
        print('It is not symmetric')
    else:
        print('it is  symmetric')
a='malayalam'
palindrome(a)
symmetric(a)








