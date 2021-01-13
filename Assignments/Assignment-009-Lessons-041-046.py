#--------------------------
#-- Mastering Python  
#-- Eighth Assignment 
#-- From Lessons 41 To 46
#--------------------------

# First assignt 
num1 = input('Enter the first num: ').strip()
num2 = input('Enter the second num: ').strip()
op = input('Enter the opertion: ').strip()
num1 = int(num1)
num2 = int(num2)
if op == '+' :
    print(num1 + num2)
elif op == '-' :
    print(num1 - num2)
elif op == '*' :
    print(num1 * num2)
elif op == '/' :
    print(num1 / num2)
elif op == '%' :
    print(num1 % num2)
else :
    print('Operation not valid')

# Second assign 

age = 9

print('App is suitable for you ' if age > 16 else 'App not suitable for you')

# Third assign

age_calculate = input('Enter your age: ').strip()
age_calculate = int(age_calculate)
if age_calculate < 10 or age_calculate > 100 :
    print("Sorry, We can't provide addetional information")
else :
    mon = age_calculate * 12 
    print(f'Your age in monthes is {mon} monthes')
    wee = mon * 4
    print(f'Your age in weeks is {wee} weeks')
    da = wee * 7
    print(f'Your age in days is {da} days')
    hour = da * 24
    print(f'Your age in hours is {hour} hours')
    min = hour * 60
    print(f'Your age in mintes is {min} mintes')
    se = min * 60
    print(f'Your age in seconds is {se} seconds')



# Fourth assign 

country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries :
    print(f'Your Country Eligible For Discount {discount} % And The Price After Discount Is $ {price - discount }')
else:
    print(f"Your Country Not Eligible For Discount And The Price Is $ {price}")