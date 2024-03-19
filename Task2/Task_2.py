# def area():
#     r=int(input('enter the radius:'))
#     Area=2*3.14*(r**2)
#     print('Area of the circle is',Area)
# area()


# number=int(input('enter a number:'))
# square_root=int(number**0.5)
# if(square_root**2==number):
#     print(number,'is a perfect square')
# else:
#     print(number,'is not a perfect square')


# string=input('enter the string:')
# alp='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in string:
#   if i in alp:
#       flag=1
#   else:
#       flag=0
# if(flag==1):
#     print('The string contain only alphabets')
# else:
#     print('the String not only contain alphabets')

#
# if(string.isalpha()):
#     print('String only contain alphabets')
# else:
#     print('string contain not only alphabets')





# def power(n,e):
#     res=1
#     for i in range(e):
#         res *= n
#     return res
# print(power(4,2))

# def power(n,e):
#     res=1
#     for i in range(e):
#         res*=n
#     return res
# print(power(4,2))

# n=4
# p=2
# power=1
# for i in range(p):
#     power*=n
# print(power)

# num=int(input('enter the decimal'))
# binary=bin(num)
# print('Binary of ',num,'is :',binary)


# string=input('Enter the String:')
# data=string.split(' ')
# lst1=[]
# lst2=[]
# for i in data:
#   lst1.append(i)
#   lst2=lst1[::-1]
# print(lst2)



# string=input('Enter the string:')
# if '@' in string:
#   if '.com' in string:
#        print('valid')
#   else:
#       print('invalid')
# else:
#   print('invalid')


#
# # Python code to demonstrate naive
# # method to compute gcd ( recursion )
#
#
# def hcf(a, b):
# 	if(b == 0):
# 		return a
# 	else:
# 		return hcf(b, a % b)
#
# a = 60
# b = 0
#
# # prints 12
# print("The gcd of 60 and 0 is : ", end="")
# print(hcf(60, 0))




# lst=[22,45,54,34,76,34,56,54,80,45]
# lst=[1,2,5,3,4]
# lst1=[]
# lst2=[]
# for i in lst:
#   if i not in lst1:
#     lst1.append(i)
#   else:
#     lst2.append(i)
# if lst2:
#   print('list contain duplicates')
# else:
#   print('list doesnot contain duplicates')



# import random
# l=int(input('Enter the password length: '))
# password=''
# for i in range(l):
#      choice=random.randint(1,3)
#      if choice==1:
#          char=chr(random.randint(65,90))
#      elif choice==2:
#          char=chr(random.randint(97,122))
#      else:
#          char=str(random.randint(0,9))
#      password+=char
# print("password=",password)





# class ToDoList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#         print(f'Task "{task}" added successfully.')
#
#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks found.")
#         else:
#             print("To-Do List:")
#             for index, task in enumerate(self.tasks, start=1):
#                 print(f"{index}. {task}")
#
#     def mark_completed(self, task_index):
#         if 1 <= task_index <= len(self.tasks):
#             completed_task = self.tasks.pop(task_index - 1)
#             print(f'Task "{completed_task}" marked as completed.')
#         else:
#             print("Invalid task index.")
#
# def main():
#     todo_list = ToDoList()
#
#     while True:
#         print("\nOptions:")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Completed")
#         print("4. Quit")
#
#         choice = input("Enter your choice (1-4): ")
#
#         if choice == "1":
#             task = input("Enter the task: ")
#             todo_list.add_task(task)
#         elif choice == "2":
#             todo_list.view_tasks()
#         elif choice == "3":
#             task_index = int(input("Enter the task index to mark as completed: "))
#             todo_list.mark_completed(task_index)
#         elif choice == "4":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")
#
# if __name__ == "__main__":
#     main()

























#
# lst=[]
# def add(task):
#   lst.append(task)
#   print('Your task',task,'is added successfully.')
# def view():
#   if not lst:
#     print('No task found')
#   else:
#     for i in lst:
#       print(i)
# def delete(task):
#   if not list:
#     print('No task to delete')
#   else:
#     lst.pop()
# while(True):
#     print('1. Add Task\n'
#           '2. View Task\n'
#           '3. Delete Task')
#     choice = int(input('Enter Your choice:'))
#     if (choice == 1):
#         task = input('enter your task:')
#         print(add(task))
#     elif (choice == 2):
#         # task=input('enter your task:')
#         print(view())
#     elif (choice == 3):
#         task = input('enter your task:')
#         print(delete(task))
#     else:
#         print('invalid choice')




# import string
# import random # define the random module
# S = 10  # number of characters in the string.
# # call random.choices() string module to find the string in Uppercase + numeric data.
# ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))
# print("The randomly generated string is : " + str(ran)) # print the random data

# import string
# import random
# length=int(input('enter the length:'))
# password="".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation,k=length))
# print('Randomly generated password with length',length,'is :',password)


my_string = "Hello, World!"

# Accessing the first character
first_char = my_string[0]
print("First character:", first_char)

# Accessing the fifth character
fifth_char = my_string[4]
print("Fifth character:", fifth_char)

# Accessing the last character
last_char = my_string[-1]
print("Last character:", last_char)
