notnumber = True
while notnumber:
    time_spent = input(
"""***NEW ENTRY***

Please enter the amount of time spent on the task, in minutes:\n> 
""")
    try:
        time_spent = int(time_spent)
    except ValueError:
        # clear_screen()
        input("You need to enter a number! Please press ENTER to try again...")
        time_spent = input(
"""***NEW ENTRY***

Please enter the amount of time spent on the task, in minutes
""")
    else:
        notnumber = False