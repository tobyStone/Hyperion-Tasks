'''
based on learning from Hyperion.dev
first compulsory task set in T15
A program to take an input of a number of
student id's and write these to a file,
along with an area for each of these id's
to sign.
'''


num_students = int(input("How many students would you like to input? "))
#with pattern to automatically close the file after use
with open("reg_form.txt", "w") as f:
    for i in range(0, num_students):
        id = input("Please enter student id number: ")
        f.write("Student ID ")
        f.write(id)
        f.write("  sign here  ..........\n")
    
