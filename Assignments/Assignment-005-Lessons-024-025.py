#--------------------------
#-- Mastering Python  
#-- Fifth Assignment  
#-- For Lessons 024 To 025
#--------------------------

# [01] Create Tuple Contain One Element Without Using The Parentheses
my_typle =  'Bishoy',

# [02] Print The Type To Be Sure Its Tuple
print(type(my_typle)) # ===> <class 'tuple'>

# [03] Create Tuple Contains 5 Friends Name The First Is "Osama"
Friends = ("Osama", "Bishoy", "Mariam", "Alessandra", "Daniella")

# [04] Use Your Knowledge To Change The First Name From "Osama" To "Elzero"
fl = list(Friends)
fl[0] = "Elzero"

# [05] Print The Tuple With The New Name
n_tuple = tuple(fl)
print(n_tuple)

# [06] Create Tuple Contain Numbers From 1 To 3 
numbers = (1, 2, 3)

# [07] Create Tuple Contain Letters From A To C
letters = ("A", "B", "C")

# [08] Concatenate The Two Tuples
col = numbers + letters
print(col)

# [09] Create New Tuple With This Result From Old Tuples (1, "A", 2, "B", 3, "C")
new_tuple = (numbers[0], letters[0], numbers[1], letters[1], numbers[2], letters[2])
print(new_tuple)

# [10] Get Number Of Elements Inside The New Tuple With 2 Methods
print(len(new_tuple))
count = 0
for i in new_tuple :
    count += 1
print(count) 

# [11] Create Tuple Contain 4 Elements ( With Any Data )
data = (True, "Bishoy", 1, 10.56)

# [12] Destruct The Tuple By Assigning Element One To Variable a And Element Two To Variable b And Element Four To Variable c
a, b, _, c = data
# [13] Print Variables a, b And c
print(a)
print(b)
print(c)