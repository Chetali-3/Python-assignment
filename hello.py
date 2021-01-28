# Making a to-do management file.

# Ask to operator
def print_name(name) :
    print("Hello"+ " " + name)
print_name(input("Please enter your name :" ))

# number of entries
number_of_entries = input("How many entries do you wanna make : ")

# Asking to operator 
fname = input("Please enter your file name with adding(.txt) : ")

# Creating a file
file = open(fname , "w")

for i in range( 0, int(number_of_entries )) :
    Task = input("Task : ")
    entry = f"{Task}\n" 
    file.write(entry)
    if i == int(number_of_entries ) - 1 :
         print("Done!")
    else :
         print("Okay, next one:")
file.close()

x = open(fname , "r")
count = 0
for line in x :
       count += 1
print(count)

#printing the file name
print(fname)
