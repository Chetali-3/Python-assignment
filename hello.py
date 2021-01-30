# Making a to-do management file.

# Ask to operator
def print_name(name) :
    print("Hello"+ " " + name)
print_name(input("Please enter your name :" ))

# Asking the operator
print("Note :-  for new Todo file, type 'new.file'  or for existing Todo file ,type 'ex.file' ")
answer = input("Please enter which file you want to open : ")
if answer == "ex.file" :
   fname = input("Please enter your existing file name: ")
# Opening the existing file and reading it
   file = open(fname, "r")
   text = file.read()
   print(text)
# asking to operate
   print(" What do you want to do now, if you want to add a ToDo type plus, for removing type cut and  for closing the file type close :")
   reply = input ("Enter your reply :")
   if reply == "plus" :
        plus = input("Type the Todo , you want to add:")
        file = open (fname , "r+")
        text = file.read()
        file.write(plus)
        file.close()                        
   elif reply == "cut" :
        cut = input("Type the index of ToDo you want to remove (note- index starts from 0) :")
        file = open(fname , "r+")
        text = file.read()
        lines = text.split("\n")
        print(lines)
        lines.pop(int(cut))
        print(lines)
        new_file = str(lines)
        file = open(fname, "w")
        file.write(new_file)
        print(file)
        file.close()
   else :
        file.close()
# Last time Reading the last time
   print(" Your new todo list :")
   file = open(fname,"r")
   text = file.read()
   print(text)
   file.close()
   print("Done! Go complete your work, all the best")
else :
# number of entries
   number_of_entries = input("How many entries do you wanna make : ")

# Asking to operator 
   fname = input("Please enter your file name with adding(.txt) : ")

# Creating a file
   file = open(fname , "w")

   for i in range(0, int(number_of_entries)) :
    Task = input("Task : ")
    entry = f"{Task}\n" 
    file.write(entry)
    if i == int(number_of_entries ) - 1 :
         print("Done!")
    else :
         print("Okay, next one:")
   file.close()
#Counting lines
   print(Total work you have to do is:)
   x = open(fname , "r")
   count = 0
   for line in x :
       count += 1
   print(count)
   print("Confirming your file name and your ToDo list : ")

#printing the file name
   print(fname)

#Reading the file
   file = open(fname , "r")
   text = file.read()
   print(text)
   print("Done! Best of luck")
