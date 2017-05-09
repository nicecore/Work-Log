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
    still_entering = True
    while still_entering:
        

        # Prompt user for task name
        task_name = input(
"""***NEW ENTRY***

Please enter the name of the task performed:\n> 
""")
        # Prompt user for time spent on {}.format(task_name)
        clear_screen()
        notnumber = True
        # While block with try/except to make sure user enters an integer
        while notnumber:
            time_spent = input(
"""***NEW ENTRY***

Please enter the amount of time spent on task "{}", in minutes:\n> 
""".format(task_name))
            try:
                time_spent = int(time_spent)
            except ValueError:
                clear_screen()
                input("You need to enter a number! Please press ENTER to try again...")
                time_spent = input(
"""***NEW ENTRY***

Please enter the amount of time spent on task "{}", in minutes
""".format(task_name))
            else:
                notnumber = False
        # Prompt user to input notes about task
        clear_screen()
        notes = input(
"""***NEW ENTRY***

Please enter any relevant notes about task "{}":\n> 
""".format(task_name))

        with open("worklog.csv", "a", newline="") as file:
            filewriter = csv.writer(file)
            filewriter.writerow([task_name, time_spent, notes])

        clear_screen()
        unchosen = True
        while unchosen:
            another_entry = input(
"""Would you like to make another entry in the work log?
Please enter Y for YES or N for NO.
""").lower()
            if another_entry == 'y' or another_entry == 'yes':
                unchosen = False
                clear_screen()
            elif another_entry == 'n' or another_entry == 'no':
                unchosen = False
                still_entering = False
                clear_screen()

    # Write these to a line on the CSV file separated by commas
    # Upon successfully writing inputs to a line of CSV file,
    # ask if user wants to make another entry
    # If not, return user to initial prompt



##########################################################################

def search_regex():
    with open("worklog.csv") as file:
        file_reader = csv.reader(file)
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
    with open("worklog.csv") as file:
        file_reader = csv.reader(file)

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
    choice = input("""
Welcome, wage slave!

Please type one of the options below and hit ENTER.

[a] Create new work log entry
[b] See all work log entries
[c] Search work log with plain text
[d] Search work log with regular expression

To cancel a new entry or a search, enter BACK
at any point during your session to return to this prompt.

""").lower()
    if choice == 'a':
        new_entry()

main()

