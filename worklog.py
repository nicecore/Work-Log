import csv
import os
import datetime
import re

# Work Log, a Treehouse Tech Degree Project
# by Adam Cameron, May 2017


def reader():
    """Return updated list of CSV file's contents"""
    with open("worklog.csv", "r") as readfile:
        reader = csv.reader(readfile)
        next(reader)
        contents = []
        for row in reader:
            contents.append(row)
        return contents


def printer(results, search):
    """Print out results of a search"""
    c_s()
    print("Results for {}:\n".format(search))
    for row in results:
        date, task, mins, notes = row
        print("""Date and time: {}
Task name: {}
Minutes spent: {}
Notes: {}

----------------------
""".format(date, task, mins, notes))

def writer(date, time, task, notes):
    """Write user input to CSV file as a new row"""
    with open("worklog.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow([date, time, task, notes])

def search_again():
    search_again = input(
"""\nWould you like to do another search?

Please press ENTER if YES, and N and ENTER if NO:
> """).lower()
    if search_again == 'n' or search_again == 'no':
        return False
    else:
        return True

def verify_num():
    """Verify that the user entered a number"""
    while True:
        c_s()
        try:
            a = int(input("Please enter a number of minutes:\n> "))
        except ValueError:
            c_s()
            input("""
Please enter a valid number!
Press ENTER to try again...""")
        else:
            return str(a)
            break

def c_s():
    """Clear screen function"""
    os.system('cls' if os.name == 'nt' else 'clear')


def new_entry():
    """Create a new work log entry"""
    c_s()
    still_entering = True
    while still_entering:
        enter_task = True
        while enter_task:
            c_s()
            task_name = input(
"""***NEW ENTRY***

Please enter the name of the task performed:\n> """)
            if task_name:
                enter_task = False
            else:
                c_s()
                input("""
Please enter a title for this task! Press ENTER to try again...
""")
        c_s()
        time_spent = verify_num()
        c_s()
        notes = input(
            """***NEW ENTRY***

Please enter any relevant notes about task "{}":
> """.format(task_name))
        entry_datetime = datetime.datetime.now()
        date_fmt = entry_datetime.strftime('%m/%d/%Y @ %-I:%M %p')
        writer(date_fmt, task_name, time_spent, notes)
        unchosen = True
        while unchosen:
            c_s()
            another_entry = input(
                """Would you like to make another entry in the work log?
Please enter Y for YES or N for NO.
> """).lower()
            if another_entry == 'y' or another_entry == 'yes':
                unchosen = False
                c_s()
            elif another_entry == 'n' or another_entry == 'no':
                unchosen = False
                still_entering = False
                c_s()
                main()


def search_regex():
    """Search CSV file contents by regular expression"""
    c_s()
    searching = True
    while searching:        # Begin while loop
        c_s()
        reg_search = input(
            """Please enter a regular expression to be searched:
> """)
        if reg_search:      # If there is reg search...
            p = re.compile(reg_search, re.IGNORECASE)
            c_s()
            results = []
            for row in reader():
                date, task, time, notes = row
                for field in row:
                    if re.search(p, field):
                        results.append(row)
            if len(results):
                printer(results, reg_search)
            else:
                print("There were no results!")
            if search_again() == False:
                c_s()
                main()
            else:
                searching = True
        else:
            c_s()
            input("Please enter a regex! Press ENTER to continue...")


def search_plain():
    """Search CSV file by a plain text phrase"""
    c_s()
    searching = True
    while searching:
        c_s()
        plain_search = input(
            """Please enter a word or phrase to search:\n> """)
        if plain_search:
            c_s()
            results = []
            for row in reader():
                date, task, time, notes = row
                for field in row:
                    if plain_search in field:
                        results.append(row)
                    elif plain_search.lower() in field:
                        results.append(row)
                    elif plain_search.upper() in field:
                        results.append(row)
                    elif plain_search.capitalize() in field:
                        results.append(row)
            if len(results):
                printer(results, plain_search)
            else:
                print("There were no results!")
            if search_again() == False:
                c_s()
                main()
            else:
                searching = True
        else:
            c_s()
            input(
"""Please enter a plain text phrase! Press ENTER to start over...""")
            c_s()


def search_date():
    """Search the CSV file by a date"""
    c_s()
    searching = True
    while searching:
        c_s()
        date_search = input(
            """Please enter a date to search in MM/DD/YYYY format:
> """)
        if date_search and re.match(r'\d\d/\d\d/\d\d\d\d', date_search):
            results = []
            for row in reader():
                date, task, time, notes = row
                if date_search in date:
                    results.append(row)
            if len(results):
                printer(results, date_search)
            else:
                print("There were no results!")
            if search_again() == False:
                main()
            else:
                searching = True

        else:
            c_s()
            input("Please enter a date! Press ENTER to start over...")
            c_s()


def search_minutes():
    """Search CSV file by the number of minutes a task took"""
    c_s()
    minute = verify_num()
    results = []
    for row in reader():
        date, task, time, notes = row
        if row[2] == minute:
            results.append(row)
    if len(results):
        printer(results, minute)
    else:
        c_s()
        print("There were no results!")
    if search_again() == False:
        c_s()
        main()
    else:
        search_minutes()


def show_all_entries():
    """Display all work log entries"""
    c_s()
    search = "ALL ENTRIES"
    results = []
    for row in reader()[::-1]:
        results.append(row)
    printer(results, search)
    input("\n\nPress ENTER to return to the main prompt...")
    main()


def main():
    """Main program prompt"""
    c_s()
    choosing = True
    while choosing:
        c_s()
        choice = input("""
Welcome, wage slave! Keep reaching for that rainbow!

This work log has been provided to you by your benevolent masters.

Please type one of the options below and hit ENTER.

[a] Create new work log entry
[b] See all work log entries
[c] Search work log with plain text
[d] Search work log with regular expression
[e] Search work log by date
[f] Search work log by time spent

[q] Quit the work log

> """).lower()
        if choice == 'a':
            choosing = False
            new_entry()
        elif choice == 'b':
            choosing = False
            show_all_entries()
        elif choice == 'c':
            choosing = False
            search_plain()
        elif choice == 'd':
            choosing = False
            search_regex()
        elif choice == 'e':
            choosing = False
            search_date()
        elif choice == 'f':
            choosing = False
            search_minutes()
        elif choice == 'q':
            quit()
        else:
            c_s()
            input("That's not a valid choice! Press ENTER to try again...")


main()
