import csv
import os
from datetime import datetime
# import

# Work Log, a Treehouse Tech Degree Project by Adam Cameron
# May 2017


# Open CSV file and create CSV object outside of functions?


##########################################################################
def clear_screen():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

##########################################################################

def new_entry():
    clear_screen()
    # Prompt user for task name
    task_name = input(
"""Please enter the name of the task performed:\n> 
""")
    
    # Prompt user for time spent on {}.format(task_name)
    time_spent = int(input(
"""Please enter the amount of time spent on the task, in minutes:\n> 
"""))

    # Prompt user to input notes about task

    notes = input(
"""Please enter any relevant notes about this task:\n> 
""")

    # Write these to a line on the CSV file separated by commas
    # Upon successfully writing inputs to a line of CSV file,
    # ask if user wants to make another entry
    # If not, return user to initial prompt

    pass


##########################################################################

def search_regex():
    
    reg_search = input(
"""Please enter a regular expression to be searched:\n> 
""")
    # Prompt user for a regular expression
    # Search CSV file for a line containing regular expression
    # Print line out to user, press ENTER to continue
    # Ask if user wants to do another regex search
    # If not, return user to initial prompt
    pass


##########################################################################


def search_plain():
    plain_search = input(
"""Please enter a word or phrase to be searched
""")
    # Prompt user for a string to search from
    # Search CSV file for a line containing the string
    # Print out entire line to user, press ENTER to continue
    # Ask if user wants to do another regex search
    # IF not, return user to initial prompt
    pass


##########################################################################


# Show intro text, which only gets displayed once, outside of main loop
# Press enter to continue -> leads to def main():

def main():
    clear_screen()
    print("""
Welcome, wage slave!

Please type one of the options below and hit ENTER.

[a] Create new work log entry
[b] See all work log entries
[c] Search work log with plain text
[d] Search work log with regular expression

To cancel a new entry or a search, enter BACK
at any point during your session to return to this prompt.

""")

