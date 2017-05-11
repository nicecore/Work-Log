import csv
import os
import datetime
import re

# Work Log, a Treehouse Tech Degree Project
# by Adam Cameron, May 2017

def printer():
    

    pass

def verify_num():
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

def date_verifier(prompt):

    pass

def verifier(prompt):

    pass

with open("worklog.csv", "a", newline="") as file:
    filewriter = csv.writer(file)


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
        # Prompt user for time spent on {}.format(task_name)
        c_s()
        notnumber = True
        while notnumber:
            time_spent = input(
                """***NEW ENTRY***

Please enter the number of minutes spent on task "{}":
> """.format(task_name))
            try:
                time_spent = int(time_spent)
            except ValueError:
                c_s()
                input("You need to enter a number! Please press ENTER to try again...")
                c_s()
            else:
                notnumber = False
        # Prompt user to input notes about task
        c_s()
        notes = input(
            """***NEW ENTRY***

Please enter any relevant notes about task "{}":
> """.format(task_name))
        entry_datetime = datetime.datetime.now()
        date_fmt = entry_datetime.strftime('%m/%d/%Y @ %-I:%M %p')
        with open("worklog.csv", "a", newline="") as file:
            filewriter = csv.writer(file)
            filewriter.writerow([date_fmt, task_name, time_spent, notes])
        c_s()
        unchosen = True
        while unchosen:
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
    """Search the CSV file by regular expression"""
    c_s()
    searching = True
    while searching:
        with open("worklog.csv", "r") as file:
            file_reader = csv.reader(file)
            reg_search = input(
                """Please enter a regular expression to be searched:
> """)
            if reg_search:
                p = re.compile(reg_search, re.IGNORECASE)
                next(file_reader)
                c_s()
                holder = []
                print("Search results for regex '{}':\n".format(reg_search))
                for row in file_reader:
                    date, task, time, notes = row
                    for field in row:
                        if re.search(p, field):
                            holder.append(field)
                            print(
                                "-{} - {}, {} minutes: {}".format(date, task, time, notes))
                if len(holder) == 0:
                    print("There were no results!")
                search_again = input(
                    """\nWould you like to do another search?

Please press ENTER if YES, and N and ENTER if NO:
> """).lower()
                if search_again == 'n' or search_again == 'no':
                    searching = False
                    c_s()
                    main()
                else:
                    c_s()
                    searching = True
            else:
                c_s()
                input("Please enter a regular expression! Press ENTER to try again...")
                c_s()

    if search_again == 'n' or search_again == 'no':
        searching = False
        c_s()
        main()
    else:
        c_s()
        searching = True


def search_plain():
    """Search CSV file by a plain text phrase"""
    c_s()
    searching = True
    while searching:
        with open("worklog.csv", "r") as file:
            file_reader = csv.reader(file)
            plain_search = input(
                """Please enter a word or phrase to search:\n> """)
            if plain_search:
                c_s()
                print("Search results for phrase '{}':\n".format(plain_search))
                results = []
                for row in file_reader:
                    date, task, time, notes = row
                    for field in row:
                        if plain_search in field:
                            results.append(plain_search)
                            print(
                                "-{} - {}, {} minutes: {}".format(date, task, time, notes))
                        elif plain_search.lower() in field:
                            results.append(plain_search)
                            print(
                                "-{} - {}, {} minutes: {}".format(date, task, time, notes))
                        elif plain_search.upper() in field:
                            results.append(plain_search)
                            print(
                                "-{} - {}, {} minutes: {}".format(date, task, time, notes))
                        elif plain_search.capitalize() in field:
                            results.append(plain_search)
                            print(
                                "-{} - {}, {} minutes: {}".format(date, task, time, notes))
                if len(results) == 0:
                    print("There were no results!")
                search_again = input(
                    """\nWould you like to do another search?

Please press ENTER if YES, or N and ENTER if NO:
> """).lower()
                if search_again == 'n' or search_again == 'no':
                    searching = False
                    c_s()
                    main()
                else:
                    c_s()
                    searching = True
            else:
                c_s()
                input("Please enter a plain text phrase! Press ENTER to start over...")
                c_s()


def search_date():
    """Search the CSV file by a date"""
    c_s()
    searching = True
    while searching:
        with open("worklog.csv", "r") as file:
            file_reader = csv.reader(file)
            date_search = input(
                """Please enter a date to search in MM/DD/YYYY format:
> """)
            if date_search and re.match(r'\d\d/\d\d/\d\d\d\d', date_search):
                results = []
                for row in file_reader:
                    date, task, time, notes = row
                    if date_search in date:
                        results.append(date)
                        print(
                            "-{} - {}, {} minutes: {}".format(date, task, time, notes))
                if len(results) == 0:
                    c_s()
                    print("There were no results!")
                search_again = input(
                    """\nWould you like to do another search?

Please press ENTER if YES, or N and ENTER if NO:
> """).lower()
                if search_again == 'n' or search_again == 'no':
                    searching = False
                    c_s()
                    main()
                else:
                    c_s()
                    searching = True
            else:
                c_s()
                input("Please enter a date! Press ENTER to start over...")
                c_s()


def search_minutes():
    """Search CSV file by the number of minutes a task took"""
    c_s()
    minute = verify_num()
    with open("worklog.csv", "r") as file:
        file_reader = csv.reader(file)
        c_s()
        print("Search results for time '{}' minutes:\n".format(minute))
        holder = []
        for row in file_reader:
            date, task, time, notes = row
            if row[2] == minute:
                holder.append(row[2])
                print(
                    "-{} - {}, {} minutes: {}".format(date, task, time, notes))
        if len(holder) == 0:
            c_s()
            print("There were no results!")
        search_again = input(
            """\nWould you like to do another search?

Please press ENTER if YES, or N and ENTER if NO:
> """).lower()
        if search_again == 'n' or search_again == 'no':
            searching = False
            c_s()
            main()
        else:
            c_s()
            search_minutes()



def show_all_entries():
    """Display all work log entries"""
    c_s()
    print("Here are all your entries, beginning with the most recent:\n")
    print("The format is [DATE and TIME] - [TASK], [TIME] minutes: [NOTES]\n")
    with open("worklog.csv", "r") as file:
        file_reader = csv.reader(file)
        next(file_reader)
        lines = [x for x in file_reader]
        for row in lines[::-1]:
            date, name, time, notes = row
            print("{} - {}, {} minutes: {}".format(date, name, time, notes))
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
