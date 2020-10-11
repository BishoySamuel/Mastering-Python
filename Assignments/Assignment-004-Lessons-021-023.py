#--------------------------
#-- Mastering Python  
#-- Fourth Assignment  
#-- For Lessons 021 To 023
#--------------------------

# [01] Create A List Contains Your Friends Names (Minimum 8 Friends)
a = ['Mido', 'Bishoy', 'Sandor', 'Fahmy', 'Samuel', 'Ibrahim', 'Osama', 'Daniol']
# Frist copy from a
fc = a.copy()
# Second copy from a
sc = a.copy()

print("=" * 50)

# [02] Print First Name In The List ( With 2 Methods )
print(fc[0])
print(fc.pop(0))

print("=" * 50)

# [03] Print Last Name In The List ( With 2 Methods )
print(fc[-1])
print(fc.pop(-1))

print("=" * 50)

# [04] Print The Even Names Only
print(f"The even names is: {sc[1::2]}")

print("=" * 50)

# [05] Print The Odd Names Only
print(f"The odd names is: {sc[::2]}")

print("=" * 50)

# [06] Print The 2, 3, 4 Names
print(sc[1:4])

print("=" * 50)

# [07] Update The 5, 6, 7 Names With The Name "Elzero"
sc[4:7] = ['Elzero']
print(sc)

print("=" * 50)

# [08] Append Two Names To The Main List 
a.append("Alex")
a.append("Mariam")
print(a)

print("=" * 50)

# [09] Create Another 2 Lists With 2 Friends And Add All This Lists To The Main List
b = ["Angy","Sally"]
c = ["Yasmine","Bossy"]
a.extend(b)
a.extend(c)
print(a)

print("=" * 50)

# [10] Remove The First Friend From The List
a.remove('Mido')
print(a)

print("=" * 50)

# [11] Remove The Last Friend From The List
a = a [0:-1]
print(a)

print("=" * 50)

# [12] Sort The List From A To Z
a.sort()
print(a)

print("=" * 50)

# [13] Sort The List From Z To A
a.sort(reverse=True)
print(a)

print("=" * 50)

# [14] Count Number Of Friends in The List ( With 2 Methods )
print(len(a))
x = 0
for n in a:
    x +=1
print(x)

print("=" * 50)

# [15] Add A New Friend in The First Place
a.insert(0,"ELking")
print(a)

print("=" * 50)

# [16] Create A Main List For You Programming Skills And Nested List From Framework
prog_sk = ["HTML", "CSS", "JS", ["Vuejs", "React", "Angular", "Gulpjs"]]

# [17] Loop on The Skills And Nested List

for i in prog_sk:
    if type(i) != list :
        print(i)
for i in prog_sk:
    if type(i) == list :
        for n in i:
            print(f"-{n}")

# Another way to loop on all strings first before loop on nested list.

for i in prog_sk:
    print(type(i))

for i in prog_sk:
    if type(i) != list:
        print(i)
    elif type(i) == list:
        for n in i:
            print(f"-{n}")

print("=" * 50)

# [18] Access The Last Skill in List ( Create Condition To Check If Its Not A List )
skills_prog = [i for i in prog_sk if type(i) != list]    
print(skills_prog[-1])

print("=" * 50)

# [19] Access The First Framework in The Nested List ( Create Condition To Check If Its A List First )
for item in prog_sk:
    if type(item) == list and len(item) >=1 :
        print(item[0])


print("=" * 50)