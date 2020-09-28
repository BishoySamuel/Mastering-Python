#-------------------------
#-- Mastering Python  
#-- Third Assignment  
#--For Lessons 019 To 020
#-------------------------

# [1] Write Down All Type Of Numbers.
print(type(100))
print(type(-10.50))
print(type(5+6j))


#[2] Get Imaginary Part For The Complex Number "1+2j".
a = 5
b= 7
print(f"The complex number for number {a} is: {complex(a)}")
print(f"The imagenary part of number {b} is: {complex(b.imag)}")

myComplexNumber = 1+2j
print(f"The Imaginary Part For The Complex Number Is: {myComplexNumber.imag}")

#[3] Get Real Part For The Complex Number "1+2j".
print(f"The Real Part For The Complex Number Is: {myComplexNumber.real}")

#[4] Convert Number 10 To Floating Point Number With Ten Numbers After Decimal.
N = 10
print("The Number Will Be {:.10f}".format(N))

#[5] Convert Number Floating Number 159.650 To Integer.
Fn = 159.650
print(int(Fn))

#[6] Function:
    #--- Create Function Accept Three Parameters (num1, num2, operation).
    #--- Check If Given Arguments Is Integers.
    #--- Return The Result Of Addition If Third Parameters Is (add, Multiply).
    #--- Get The Same result Without Use The Exponents 3**8.
def Add(num1,num2,ope):
    if type(num1) != int or type(num2) != int:
        print("Kindly Enter Integers Numbers")
    else:
        if ope == "+":
            print(num1 + num2)
        elif ope == "*":
            print(num1 * num2)
        elif ope == "**":
            print(8 * (num1 * num1))

Add(5,6,"+")
Add(5,6,"*")
Add(3,8,"**")

#[7] Get The Same result Without Use The Exponents 3**8.
Result = lambda x,y: x**y
print(Result(3,8))

#[8] Whats the Different Between 21/2 And 21//2.
print(21/2) # 21/2 = 10.5 ==> Is Divison.
print(21//2) # 21//2 = 10 ==> Is Floor Division.