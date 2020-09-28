#-------------------------
#-- Mastering Python  
#-- Second Assignment  
#--For Lessons 011 To 018
#-------------------------

NAME = "Bishoy"
AGE = 37
COUNTRY = "Egypt"

print('Hello %s, How You Doing \\\"Your Age is %d"' % (NAME, AGE))

print("Hello {:s},How You Doing \\\"Your Age is {:d}\"".format(NAME, AGE))

print(f"Hello {NAME},\nHow You Doing\\\n\"Your Age is {AGE}\"")

BOSS = "Elzero"

print(BOSS[1])
print(BOSS[-1])
print(BOSS[1:4])
print(BOSS[::2])
print(BOSS[-2::-2])

OSAMA = "#@#@Elzero#@#@"
print(OSAMA.strip("#@",))

def ZFILL(*numbers):
    for n in numbers:
        print(n.zfill(4))
ZFILL("5", "95", "998", "9999")

def HASH(name):
    a = 20 - len(name)
    if len(name) < 20:
        print(("#" * a) + name)
        #print(f"(# *{a}){name}") why False ???
    else:
        print(name)
HASH("Bishoy")

My_Boss = "OSamA"
print(My_Boss.swapcase())

My_String = " I Love Python And Although Love Elzero Web School"
print(My_String.count("Love"))
print(My_String.index("z"))
print(My_String.find("z", 0, 40))

MyStringOne = "I <3 Python And Although <3 Elzero Web School"
print(MyStringOne.replace("<3", "Love", 1))
print(MyStringOne.replace("<3", "Love"))

print(f"Hello {NAME},How You Doing\\\" Your Age is {AGE}\"")
