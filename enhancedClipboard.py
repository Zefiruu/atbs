#! python3 
# enhancedClipboard - A program to fetch text and save to clipboard

# Imports #
import sys, pyperclip

# Variables #
shortcuts = {     # List of shortcuts
            'hi': 'Hello team, please note we have encountered the following issues:',
            'best':'Best Regards,\nPatrick\nMicrosoft Commercial Support'
            }

# Logic #

if len(sys.argv) < 2: # Prompt in case user forgot to input arguments
    print('Usage:\n  python3 enhancedClipboard.py [shortcut]')
    sys.exit()
shortcut = sys.argv[1]  # Argument for command line

if shortcut in shortcuts: # Search if argument input by user exists 
    pyperclip.copy(shortcuts[shortcut])
    print('The text under shortcut "' + shortcut + '" is copied to clipboard.')
else:
    print('No shortcut registered yet for' + shortcut)
