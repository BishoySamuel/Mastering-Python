# #--------------------------
# #-- Mastering Python  
# #-- Eighth Assignment 
# #-- From Lessons 47 To 50
# #--------------------------

# # First assignmnet

# num = input("Enter any number more than '0' : ")
# num = int(num)
# count = 0
# if num <= 0:
#     print("The Number no longer than 'zero'")   
# while num > 0 :
#     num -= 1   
#     if num == 0:
#         break
#     elif num == 6:
#         continue
#     count +=1
#     print(num)
# print(f"{count} Numbers printed succesfully.")
    
# # Second assignment

# myFriends = ["bishoy", "maria", "Daniella", "Alessandra", "mariam"]

# count = 0
# index = 0
# while len(myFriends) > index:
#     if myFriends[index].islower():
#         index += 1
#         count += 1
#         continue
#     else:
#         print(myFriends[index])
#         index += 1
# print(f"Capitals names printed, and {count} names ignored")

# # Third assignment

# skills = ["HTML", "CSS", "JS","PHP", "Python"]
# while skills:
#     print(skills.pop(0))
    
# # Fourth assignment

my_friends = list()
max_friends = 4
while len(my_friends) < 4 :
    name = input("Add Name: ").strip()
    if name == name.upper():
        print("Invalid Name.")
    elif name == name.lower():
        name_capitalize = name.capitalize()
        my_friends.append(name_capitalize)
        max_friends -= 1
        print("The name changed to be capitalized.")
        print(f"{name_capitalize} was added, {'Add the last' if max_friends == 1 else max_friends} name left")    
    elif name == name.capitalize():
        my_friends.append(name)
        max_friends -= 1
        print(f"{name} was added, {'Add the last' if max_friends == 1 else max_friends} name left")
    elif max_friends == 0 :
        print("List is full")
else:
    print("Your List Is Full")
       
print(my_friends)