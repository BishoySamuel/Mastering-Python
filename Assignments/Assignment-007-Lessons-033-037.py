#--------------------------
#-- Mastering Python  
#-- Seventh Assignment 
#-- From Lessons 33 To 37
#--------------------------

# Print to output 4 'True' values by bool method.
print(bool(" "))
print(bool(-100))
print(bool((1,2)))
print(bool('Bishoy'))

# Print to output 4 'False' values by bool method.
print(bool(""))
print(bool(0))
print(bool(None))
print(bool([]))

# Without Using if condition, check if all variables more than 50% 
Css = 60
Html = 51
JS = 52
print(Css > 50 and Html > 50 and JS > 50)

# Third one 
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

# Forth one

num_one = 10
num_two = 20
result = num_one + num_two
print(result)
print(result**3)
print(result**3 % 2600)
print(result**3 % 2600 / 5)
print(str(result**3 % 2600 / 5))
print(type(str(result**3 % 2600 / 5)))