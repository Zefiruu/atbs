#! python3
#  bullet_point.py -  Add bullet points to list and save on clipboard

# Imports #
import sys, pyperclip

# Variables #
user_input = pyperclip.paste() # String saved in User's clipboard once the script is initiated
user_list = user_input.split('\n') # Splitting and converting string to list
bullet_list = [] # List containing * at the beginning of User's clipboard

# Logic #
for i in user_list:
    bullet_list.append('* ' + i)

pyperclip.copy('\n'.join(bullet_list)) # Saving parsed list to User's Clipboard


# Test #
''' 
Copy the following list, run code then ctrl+v anywhere to see if it's working:

Apple1 
Apple2
Apple3
Apple4
Apple5
Apple6
Apple7
'''