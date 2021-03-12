# --------------------------
# -- Mastering Python  
# -- Eleventh Assignment 
# -- From Lessons 51 To 55
# --------------------------

# # First Assign 

# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_sorted_nums = sorted(my_nums, reverse=True)

# a = 0     
# for num in my_sorted_nums:
#     if num % 5 == 0:
#         a+=1
#         print(f'{a} => {num}')
# else:
#     print("All Numbers Printed")
# print("\n##### End Of Assignment 1 #####\n")

# # Second Assign 

# for num in range(1, 21):
#     if num == 6 or num == 8 or num == 12:
#         continue
#     elif num < 10:
#         num = str(num)
#         strnum = num.zfill(2)
#         print(strnum)
#     else:
#         print(num) 
# print("\n##### End Of Assignment 2 #####\n")    

# # Third Assign    

# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }

# count = 0
# degree = 0
# for item in my_ranks:
#     if my_ranks[item] == 'A':
#         degree = 100
#         count+=degree
#     elif my_ranks[item] == 'B':
#         degree = 80
#         count+=degree
#     else:
#         degree = 40   
#         count+=degree 
#     print(f'My Rank in {item} Is {my_ranks[item]} And This Equal {degree} Points')
# print(f"Total Points Is {count}")
# print("\n##### End Of Assignment 3 #####\n")

# Forth Assign

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}


# for name in students:
#     total = 0
    
#     print(f"\n-------------------------\n-- Student Name => {name}\n-------------------------")

#     for item in students[name]:

#         if students[name][item] == 'A':
#             student_degree = 100
#             total+=student_degree   

#         elif students[name][item] == 'B':
#             student_degree = 80
#             total+=student_degree   

#         elif students[name][item] == 'C':
#             student_degree = 40
#             total+=student_degree   

#         elif students[name][item] == 'D':

#             student_degree = 20
#             total+=student_degree   

#         print(f'- {item} => {student_degree} Points')
#     print(f'Total Points For {name} Is {total}')

# # items() methods solution

for m_key, m_value in students.items():
    total = 0
    print(f"\n-------------------------\n-- Student Name => {m_key}\n-------------------------")

    for key, value in m_value.items():
        if value == 'A':
            student_degree = 100
            total+=student_degree
        elif value == 'B':
            student_degree = 80
            total+=student_degree
        elif value == 'C':
            student_degree = 40
            total+=student_degree
        elif value == 'D':
            student_degree = 20
            total+=student_degree
        print(f'-{key} => {student_degree} points')
    print(f'Total Points For {m_key} Is {total}')
print("\n##### End Of Assignment 4 #####\n")