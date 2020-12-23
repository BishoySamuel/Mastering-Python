# #--------------------------
# #-- Mastering Python  
# #-- Eighth Assignment 
# #-- From Lessons 38 To 40
# #--------------------------

# # First Assign
# name = input('Enter your name: ').strip().capitalize()
# print('Welcome', name)

# # Second Assign 
# age = input('Enter your age: ').strip()
# age = int(age)
# if age < 16 :
#     print('Worning, Your Age Is Under 16, Some Articles Is Not Suitable For You')
# else :
#     print(f'Welcome to our website {name}, because your age is {age}, so you are acceptable')

# # Third Assign
# f_name = input('Enter your first name: ').strip().capitalize()
# s_name =  input('Enter your Second name: ').strip().capitalize()
# print(f'Welcome {f_name} {s_name:.1s}')

# Fourth Assign  
mail = input('Enter your e-mail: ').strip().lower()
user_name = mail[:mail.index('@')]
print(f"Your user name is : {user_name}")
y_mail = mail[mail.index('@') + 1 : ]
print(f"Your Mail on {y_mail}")
domain = y_mail[y_mail.index('.') + 1 : ]
print(f'Your top domain in "{domain}"')
