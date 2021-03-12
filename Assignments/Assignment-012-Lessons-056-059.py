# --------------------------
# -- Mastering Python  
# -- Twelfth Assignment 
# -- From Lessons 56 To 59
# --------------------------

# First Assign 

def calculate(n1, n2, op):
    
    if op == '+' or op.capitalize().startswith('A') :
        return n1 + n2
    elif op == '-' or op.capitalize().startswith('S'):
        return n1 - n2
    elif op == '*' or op.startswith('m') or op.startswith('M'):
        return n1 * n2
    elif op == '':
        return n1 + n2
    else:
        return "Sorry it's not valid operation"

print(calculate(8, 4, 'sa'))
print('\n### The end of the first assign ###\n')


# Second Assign

def addition(*numbers):

    total = 0
    for num in numbers:
        if num == 10:
            continue
            
        elif num == 5:
            total-=num
            
        else:
            total+=num
    return total
            
    

print(addition(10, 20, 30, 10, 15))
print(addition(10, 20, 30, 10, 15, 5, 100))
print('\n### The end of the second assign ###\n')

# Third assign

#-------
# Any code after [returen] will not run
#-------

def show_skills(name, *skills):

    if len(skills) == 1:
        print(f"Hello {name}, your skill is: ")

    elif len(skills) > 1:
        print(f"Hello {name}, your skills is: ")

    else:
        print(f"Hello {name}, you don't have any skill yet")

    for skill in skills:
        print(skill)
            

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills('Ahmed')
show_skills('Bishoy', 'Python')
print('\n### The end of the third assign ###\n')
# Forth assign

def say_hello(name ='Unknown', age = 'Unknown', country = 'Unknown'):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"

print(say_hello("Osama", 38, "Om El Donia"))
print(say_hello())
print('\n####################\n')