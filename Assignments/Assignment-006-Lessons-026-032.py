#--------------------------
#-- Mastering Python  
#-- Fifth Assignment  
#-- From Lessons 26 To 32
#--------------------------

# [01] Create A List Contains 1, 2, 3, 3, 4, 5, 1
num_list = [1, 2, 3, 3, 4, 5, 1]

# [02] Loop on List And Return The Unique Values Only ( We Need TO Use Set )
num_set = set()
for num in num_list :
    num_set.add(num)
print(list(num_set))

# [03] Convert The Result To Set And Loop on This Set And Exclude The Last Element From Loop
for i, item in enumerate(num_set):
    if i == len(num_set) - 1 :
       break
    print(item)

# [04] Create Two Sets Contains 1, 2, 3, 4 And Second One A, B, C, D
set_one = {1, 2, 3, 4}
set_two = {'A', 'B', 'C', 'D'}

# [05] Merge The Two Sets With 4 Methods

print(set_one | set_two)

fm = set_one.union(set_two)

print(fm)

set_one.update(set_two)
print(set_one)

for number in set_one :
    set_two.add(number)
print(set_two)

# [06] Create Set Contains 1, 2, 3, 4 And Add List Contains A, B, C To It
new_set = {1, 2, 3, 4}
new_list = ['A', 'B', 'C']
new_set.update(new_list)
print(new_set)

# [07] Create Set Contains 1, 2, A, B And Other Set Contains 1, 2
Set_One = {1, 2, 'A', 'B'}
Set_Two = {1, 2}

# [08] Check if All Elements in Set Two Is Found in Set One Or No
print(Set_Two.issubset(Set_One))

# [09] Create Multi-Dimensional Dictionary Contains Your 4 Skills With Name And Progress
lang_skills = {
    'One' : {
        'Python' : '25 %'
    },
    'Two' : {
        'English' : '80 %'
    },
    'Three' : {
        'Deutch' : '70 %'
    },
    'Four' : {
        'Arabic' : '90 %'
    }
}

# [10] Loop on The Keys Of The Dictionary And Count Number Of Elements Inside It
for key in lang_skills :
   print(f"The key '{key}' include '{len(lang_skills[key])}' element")

# [11] Loop on The Values Of The Dictionary And Count Number Of Elements Inside It
for k, v in lang_skills.items() :
   print(f"The value for the '{k}' is: '{v}' include '{len(lang_skills[k])}' element")
   

# [12] Loop on The Keys + Value in The Same Time And Add ( - ) Between Them
for k in lang_skills :
   print(k)
   for v in lang_skills[k] : 
      print(f'- {v}')

for key, value in lang_skills.items() : 
   print(key)
   for k, v in value.items() :
      print(f'{k}-{v}')

# [13] Get All Items Inside Dictionary Without Using Loop

print(lang_skills.items())

# [14] Add New Skill To The Dictionary And Be Sure Previous Step Get And New Skill You Add
five_skill = {
    "Five" : {
        'French' : '60 %'
    }
}

lang_skills.update(five_skill)
print(lang_skills.items())

# [15] Create List Contains Your 5 Skills Names
skills_key = ['Management', 'Sales', 'Teamworke', 'Networking', 'Creative Thinking', 'koko']

# [16] Create Tuple Contains Your 5 Skills Progress 
progress_value = ('90%', '95%', '85%', '70%', '80%')

# [17] Create Multi-Dimensional Dictionary From The List + Tuple You've Created 
skills_dict = dict(zip(skills_key, progress_value))
print(skills_dict)

# [18] Make One Of The Skills Progress Less Than 50%
skills_dict['Networking'] = '49%'
print(skills_dict)
skills_dict.update({'Networking': '48%'})
print(skills_dict)

# [19] Loop on All Skills And Exclude Any Skill Less Than 50%
for k, v in skills_dict.items():
    if v < '50%' :
        continue
    print(k)
   
# [20] Create Dictionary Contains Numbers Between 1 And Given Number => { Number: Number * Number }
num_dict = dict()

numbers = range(1, 21, 2)
for number in numbers :
    num_dict.update({number: number * number})
print(num_dict)

# [21] Create Dictionary Contains Skills ( HTML, CSS, JS ) And Nother One Contains ( PHP, Python )
one = {'HTML': '0%', 'CSS': '10%', 'JS': '20%'}
two = {'PHP': '05%', 'Python': '30%'}

# [22] Merge The Two Dictionaries And Sort The Skills Reversed Then Loop on All Skills
all_dict = one.copy()
all_dict.update(two)

all_items = sorted(all_dict.items(), reverse=True)
print(all_items)
l = []
for k, v in all_items:
    l.append((v, k))
print(sorted(l, reverse=True))

# [23] Create Dictionary Contains Random Numbers From 1 To 20
ran_dict = dict()
import random

for i in range(1,5):
    n = random.randint(1,20)
    ran_dict.update({n:i})
print(ran_dict)

# [24] Return The Maximum Value And Minimum Value in The Dictionary Value
bigcount = None
mincount = None
bigi = None
for m, count in ran_dict.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        #bigi = m
    if mincount is None or count < mincount :
        mincount = count
print('The Maximum Value is:', bigcount)
print('The Minimum Value is:', mincount)

# [25] Create Dictionary With Values 1, 2, 2, 2, 3, 3, 5, A, B, C 
friends = ['Bishoy', 'Emad', 'Rezk', 'Ibrahim', 'Fahmy', 'Samuel', 'Sandor', 'Daniel', 'Maria', 'Mariam']
dict_value = [1, 2, 2, 2, 3, 3, 5, 'A', 'B', 'C']
final_dict = dict(zip(friends, dict_value))
print(final_dict)

# [26] Loop On Dictionary And Return Unique Values Only
unique_v = set()
for f, v in final_dict.items() :
    unique_v.add(v)
print(unique_v)
