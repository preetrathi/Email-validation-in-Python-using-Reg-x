# Import the 're' module for regular expressions
import re

# Define the email validation regular expression pattern
email_condition = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

# Prompt the user to input their email address and store it in the 'email' variable
email = input("Enter your email: ")

# Use 're.search()' to search for a match between the input email and the regex pattern
if re.search(email_condition, email):
    # If a match is found, print "Email is Valid"
    print("Email is Valid")
else:
    # If no match is found, print "Invalid Email"
    print("Invalid Email")
