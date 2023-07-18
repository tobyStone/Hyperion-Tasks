'''
based on learning from Hyperion.dev
first compulsory task set in T18
A program to set up an email class, pre-populate instances of this
with details of sender, subject line and content
and store these in a list. Once stored, the program
offers services such as reading specific emails
and reading all unread emails, changing the variable
of whether the emails have been read as it does so.
This is a resubmit. The read email option now
prints a numbered list of emails and subject lines
for the user to choose from. Thanks to Kelcey Webb
for feedback on this task.
'''


### --- OOP Email Simulator --- ###

import sys

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:

    # Declare the class variable, with default value, for emails.

    has_been_read = False


    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

         
 


    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):

        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox(inbox):
    
    # Create 3 sample emails and add it to the Inbox list. 

    email1 = Email('peter@stuff.com', 'stuff to do', 'a list of things')
    email2 = Email('petra@stuff.com', 'more stuff to do', 'a second list of things')
    email3 = Email('phillipa@stuff.com', 'nothing to do', 'you can ignore this')
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)




def list_emails(inbox):
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.

    for count, i in enumerate(inbox, start = 1):
        print(count, "   ", i.subject_line)
#        counter += 1

def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.


    for count, i in enumerate(inbox, start = 1):
        if count == index:
            print(i.email_content)
            i.mark_as_read()
            print(f"\nEmail from {i.email_address} marked as read.\n")

    #counter = 1
    #for i in inbox:
    #    if counter == index:
    #        print(counter, "   ", i.email_address, "   ", i.subject_line, "   ", i.email_content)
    #        i.mark_as_read()
    #        print(f"\nEmail from {i.email_address} marked as read.\n")
    #    counter += 1

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

populate_inbox(inbox)

# Fill in the logic for the various menu operations.
def read_unread_emails():

    counter = 1
    for i in inbox:
        if i.has_been_read == False:
            print(counter, "   ", i.email_content)
            counter += 1

menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        list_emails(inbox)
        selected_email = int(input("Please input the number of the email you wish to read: "))
        read_email(selected_email)

    elif user_choice == 2:
        # add logic here to view unread emails
        read_unread_emails()
        
    elif user_choice == 3:
        # add logic here to quit appplication
        print("Goodbye")
        sys.exit(0)

    else:
        print("Oops - incorrect input.")
