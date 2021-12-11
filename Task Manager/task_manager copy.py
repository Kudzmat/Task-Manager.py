# This program will manage tasks for members of a team
# It will ask users to login using a username and password
# Users will have access to various features including registering a new user as well as adding and viewing tasks

import datetime
import time
from datetime import date  # this will give us today's date when adding a task

today = date.today()  # this variable will used for today's date
today_2 = today.strftime("%Y %m %d")  # to get a different format of the date
logged_in = False  # this variable will check if a user is logged in or not
admin_logged = False  # this variable will check if admin is logged in
user_reg = False  # this variable will check if a user is registered
add_task = False  # this variable will check if a valid username has been used to add a task

usernames = ""  # this variable will store all the usernames
passwords = ""  # this variable will store all the passwords
task_view = ""  # this string is for viewing all the tasks
your_task = ""  # this string is for viewing a user's tasks


# This function will read the data in users.txt and return a dictionary for use in the program
def user_data():
    with open("user copy.txt", 'r') as users:
        my_dict = {}
        for lines in users.readlines():
            lines2 = lines.strip()  # to remove the white spaces on the passwords
            lines2 = lines.split(',')  # to remove the comma next to the username
            lines2 = "".join(lines2)
            lines2 = lines2.strip()
            lines2 = lines2.split()
            my_dict[lines2[0]] = lines2[1]  # creating a dictionary with usernames and passwords
    return my_dict


# This function will read the data from the task file and store it in a list for use in the program

def task_list():
    my_list = []
    with open("tasks copy.txt", 'r') as file:
        for lines in file.readlines():
            tasks = lines.split(',')
            my_list.append(tasks)
    return my_list  # allows the list to be used by other functions


# This function will check for usernames and prevent any duplication
def reg_user():
    users = user_data()  # calling users and passwords dictionary
    registered = False

    while registered == False:
        new_name = input("Enter a new username: ")
        new_word = input("Enter a new password: ")
        word_verify = input("Please re-enter your password: ")
        registered = True

    if new_name in users.keys():
        print("This username is already in use.")
        registered = False
    elif new_word != word_verify:
        print("Passwords do not match, please try again.")
        registered = False

    else:
        print("username does not exist.")

    while registered == True:
        with open("user copy.txt", "a") as f:
            f.write("\n" + new_name + "," + " " + new_word)
            # usernames += new_name  # add to usernames
            print(f"Congratulations, {new_name} has been registered.")
            break


def task_add():
    users = user_data()
    add_task = False

    while not add_task:
        name_task = input("Enter the username for the person the task is assigned to:  ")

        if name_task in users.keys():
            add_task = True

        else:
            print("A username must be registered before being assigned a task.")
            add_task = False

    while add_task == True:
        task_title = input("Enter the name of the task: ")
        print('')  # empty string for presentation and readability purposes
        task_description = input("Enter a short description of the task: ")
        year = int(input('Enter the year this task is due (YYYY): '))
        month = int(input('Enter the month this task is due (MM): '))
        day = int(input('Enter the day this task is due (DD): '))
        task_due = datetime.date(year, month, day)
        if task_due < today:
            print("The Due date cannot be before today's date.")
        elif task_due > today:
            with open("tasks copy.txt", 'r+') as tasks:
                for task in tasks.readlines():
                    tasks2 = task.strip()
                    tasks2 = tasks2.split(',')
                tasks.write("\n" + name_task + ", " + task_title + ", "
                            + task_description + ", " + str(today) + ", " + str(task_due) + ", No")
                print("Task has successfully been added.")
                break


def view_all():
    i = 0
    my_list = []
    my_list = []
    task = task_list()  # call function to get task list
    my_list.append(task)
    while i < len(task):
        for item in task:
            print("\nUSER - " + task[i][0] + "\nTASK - " + task[i][1] + "\nTASK DESCRIPTION - " + task[i][2] +
                  "\nDATE ASSIGNED - " + task[i][3] + "\nDUE DATE - " + task[i][4] + "\nCOMPLETED - " + task[
                      i][5])
            i += 1


def view_mine():
    i = 0
    n = 1  # this will number each task
    list2 = []
    task = task_list()  # calling list with tasks
    while i < len(task):
        if name in task[i][0]:
            print(str(n) + "\nUSER - " + task[i][0] + "\nTASK - " + task[i][1] + "\nTASK DESCRIPTION - " + task[i][2] +
                  "\nDATE ASSIGNED - " + task[i][3] + "\nDUE DATE - " + task[i][4] + "\nCOMPLETED - " + task[
                      i][5])
            list2.append(task[i])  # appending all the name tasks into a new list
            n += 1
        else:
            pass
        i += 1
        print('')

    option = int((input("Press a number to select a task or presss '-1' to go back: ")))

    if option == -1:
        pass
    else:
        option2 = int(input('''
         Please select an option:

        1) Mark as complete

        2) Edit task'''))

        if option2 == 1:
            option = int(option) - 1  # to get the index
            x = task.index(list2[option])  # finding the index in task list by matching the 2 lists
            task[x].pop()  # removing the last item in the list
            task[x].append(" Yes\n")  # adding the new item
            print("This Task has now been completed.")

            # writing back the updated task list to the file
            with open("tasks copy.txt", 'w') as final:
                i = 0
                while i < len(task):
                    for item in task:
                        final.write(task[i][0] + "," + task[i][1] + ","
                                    + task[i][2] + "," + task[i][3] + "," + task[i][4] + "," + task[i][5])
                        i += 1

        elif option2 == 2:
            option = int(option) - 1  # to get the index
            x = task.index(list2[option])
            if task[x][5] == " Yes":  # if last index is 'yes' we cannot edit this task
                print('Only a task that has not been completed can be edited.')
            else:
                option3 = int(input('''What would you like to do:
                1. Change the username for a task
                2. Change the Due Date for a task

                :'''))
                if option3 == 1:
                    users = user_data()  # calling dictionary with all users
                    new_name = input("Enter the username you would like to assign this task to: ")
                    if new_name in users.keys():
                        x = task.index(list2[option])
                        task[x].pop(0)
                        task[x].insert(0, new_name)  # changing the index from our task list
                        print("User name change successful.")

                        # After editing my list, I will write back the updated list into my txt file
                        with open("tasks copy.txt", 'w') as final:
                            i = 0
                            while i < len(task):
                                for item in task:
                                    final.write(task[i][0] + "," + task[i][1] + ","
                                                + task[i][2] + "," + task[i][3] + "," + task[i][4] + "," + task[i][
                                                    5])
                                    i += 1
                    else:
                        print("A task can only be assigned to a registered user.")

                elif option3 == 2:
                    year = int(input('Enter a year (YYYY): '))
                    month = int(input('Enter a month (MM): '))
                    day = int(input('Enter a day (DD): '))
                    new_date = datetime.date(year, month, day)
                    if new_date < today:
                        print("The Due date cannot be before today's date.")
                    elif new_date > today:
                        x = task.index(list2[option])
                        task[x].pop(4)
                        task[x].insert(4, str(new_date))
                        print("Date change successful.")

                        with open("tasks copy.txt", 'w') as final:
                            i = 0
                            while i < len(task):
                                for item in task:
                                    final.write(task[i][0] + "," + task[i][1] + ","
                                                + task[i][2] + "," + task[i][3] + "," + task[i][4] + "," + task[i][
                                                    5])
                                    i += 1


def generate():

    # Finding total task count
    tasks = task_list()
    task_count = 0
    for count, item in enumerate(tasks):
        task_count += 1

    # Finding the total number of completed tasks
    i = 0
    complete_tasks = 0
    tasks2 = []

    while i < len(tasks):
        tasks2.append(tasks[i][5])  # create a list with all the last indexes
        i += 1

    tasks2 = ",".join(tasks2)
    tasks2 = tasks2.split()
    for item in tasks2:
        if item == "Yes":  # counting all the yes responses
            complete_tasks += 1

    # Finding uncompleted tasks
    i = 0
    incomplete_tasks = 0
    tasks2 = []

    while i < len(tasks):
        tasks2.append(tasks[i][5])
        i += 1

    tasks2 = ",".join(tasks2)
    tasks2 = tasks2.split()
    for item in tasks2:
        if item == "No":
            incomplete_tasks += 1

    incomplete_perc = (incomplete_tasks / task_count) * 100
    incomplete_perc = round(incomplete_perc, 2)

    # Finding overdue and incomplete
    i = 0
    overdue = 0

    while i < len(tasks):
        for item in tasks:
            new_day = tasks[i][4]
            new_day = new_day.strip()  # to get rid of the space in the date
            if new_day < today_2 and tasks[i][5] == " No\n":
                i += 1
                overdue += 1
            else:
                i +=1

    # Finding overdue %

    overdue_perc = (overdue / task_count) * 100
    overdue_perc = round(overdue_perc, 2)

    with open("task_overview.txt", 'w') as to:
        to.write(f'''
        -----TASK OVERVIEW REPORT-----
        A total of {task_count} task(s) have been generated and tracked
        A total of {complete_tasks} task(s) have been completed
        A total of {incomplete_tasks} task(s) have not been completed
        A total of {overdue} task(s) are overdue
        {str(incomplete_perc)}% of tasks are incomplete
        {str(overdue_perc)}% of tasks are overdue
        ''')

    users = user_data()  # calling dictionary of usernames

    # Getting the total number of users

    i = 0
    user_total = 0
    while i < len(users):
        for items in users.values():
            i += 1
            user_total += 1


    # Getting the number of tasks assigned to each user

    i = 0
    n = 1
    user_num = {}  # this dictionary will hold the usernames and the number of tasks each user has
    user_num2 = {}
    user_list = []  # this list will hold the names of users for every time they appear in a task

    while i < len(tasks):
        user_list.append(tasks[i][0])  # append the users into a separate list
        i += 1

    while n < len(users.keys()):
        for item in users.keys():
            x = user_list.count(item)  # find how many times each user appears in the list
            user_num[item] = x  # set the user as the key and number of appearances as the value
            n += 1


    # Getting the user completed tasks and percentage
    i = 0
    complete = {}  # this dictionary will have users and their completion percentage
    my_list = []  # this list will have all users with a completed task
    while i < len(tasks):
        for item in tasks:
            if tasks[i][5] == " Yes\n" or tasks[i][5] == " Yes":
                my_list.append(tasks[i][0])  # make a list of the names with a yes
                i += 1
            else:
                i += 1
    for item in users.keys():
        x = my_list.count(item)  # find how many times a user has 'yes'
        complete[item] = x  # user & completion percentage

    # Calculating the percentage of completed tasks each user has
    yes_percent = []  # this list will hold the percentage of completed tasks for each user
    yes_list = []  # this list will hold the total number of completed tasks for each user
    user_nums = []  # this list will hold the total number of tasks for each user
    yes_percent2 = {}  # this dictionary will hold the username and completion percentages each user

    for key, value in complete.items():
        yes_list.append(value)  # putting the number of yeses into one list

    for key, value in user_num.items():
        user_nums.append(value)  # putting the total number of tasks into one list

    i = 0
    while i < len(yes_list) and i < len(user_nums):
        if yes_list[i] == 0 or user_nums[i] == 0:  # this is to avoid 0 division errors
            yes_percent.append(0)
            i += 1
        else:
            result = (yes_list[i] / user_nums[i]) * 100  # divide each users incompletion number and task total x 100
            result = round(result, 2)
            yes_percent.append(result)  # append each number to the list
            i += 1

    i = 0
    while i < len(yes_percent):
        for item in users.keys():
            yes_percent2[item] = yes_percent[i]  # creating dictionary with username and their completion rate
            i += 1

    # Similar logic will be applied to find the incompletion rates

    i = 0
    incomplete = {}
    my_list = []
    while i < len(tasks):
        for item in tasks:
            if tasks[i][5] == " No\n" or tasks[i][5] == " No":
                my_list.append(tasks[i][0])  # make a list of the names with a no
                i += 1
            else:
                i += 1
    for item in users.keys():
        x = my_list.count(item)  # find how many times a user has 'No'
        incomplete[item] = x  # user & incompleteion percentage

    # Calculating the percentage of incompleted tasks each user has
    no_percent = []  # this list will hold the percentage of incompleted tasks for each user
    no_list = []  # this list will hold the total number of incompleted tasks for each user
    user_nums = []  # this list will hold the total number of tasks for each user
    no_percent2 = {}  # this dictionary will hold the username and incompletion percentages each user

    for key, value in incomplete.items():
        no_list.append(value)  # putting the number of nos into one list

    for key, value in user_num.items():
        user_nums.append(value)  # putting the total number of tasks into one list


    i = 0
    while i < len(no_list) and i < len(user_nums):
        if no_list[i] == 0 or user_nums[i] == 0:  # this is to avoid 0 division errors
            no_percent.append(0)
            i += 1
        else:
            result = (no_list[i] / user_nums[i]) * 100  # divide each users incompletion number and task total x 100
            result = round(result, 2)
            no_percent.append(result)  # append each number to the list
            i += 1

    i = 0
    while i < len(no_percent):
        for item in users.keys():
            no_percent2[item] = no_percent[i]  # creating dictionary with username and their completion rate
            i += 1



    # Getting the user incomplete and overdue percentage
    i = 0
    late_count2 = []  # this list will contain the number of times a user appears in the late task list
    late_tasks = []  # this list will contain all the users with late tasks

    # Get all the dates
    while i < len(tasks):
        for item in tasks:
            new_day = tasks[i][4]
            new_day = new_day.strip()
            response = tasks[i][5]
            response = response.strip()
            if new_day < today_2 and response == "No" :
                late_tasks.append(tasks[i][0])  # all the late users
                i += 1
            else:
                i += 1

    # find how many times a user appears in late tasks list
    for name in users.keys():
        x = late_tasks.count(name)
        late_count2.append(x)

    i = 0
    user_tasks_no = []  # this list will contain each user's total number of tasks
    late_percent = []  # this list will contain each user's late percentage rate
    late_percent2 = {}  # this dictionary will have the usernames and later percentage rates
    for item in user_num.values():
        user_tasks_no.append(item)

    while i < len(user_tasks_no) and i < len(late_count2):
        if late_count2[i] == 0 or user_tasks_no[i] == 0:  # this is to avoid 0 division errors
            late_percent.append(0)
            i += 1
        else:
            result = (late_count2[i] / user_tasks_no[i]) * 100  # divide each users incompletion number and task total x 100
            result = round(result, 2)
            late_percent.append(result)  # append each number to the list
            i += 1

    i = 0
    while i < len(late_percent):
        for user in users.keys():
            late_percent2[user] = late_percent[i]
            i += 1





    with open("user_overview.txt", 'w') as uo:
        uo.write(f"        \n-----USER OVERVIEW REPORT-----\nA total of {user_total} user(s) have been registered.\nA total of {task_count} task(s) have been generated and tracked.")

        for key,value in user_num.items():  # number of taks asssigned
            uo.write(f"\n{key} has {value} task(s) assigned to them.")

        for key,value in user_num2.items():  # percentage of tasks assigned
            uo.write(f"\n{key} has {value}% of the tasks assigned to them.")

        for key,value in yes_percent2.items():  # percentage of tasks the user has completed
            uo.write(f"\n{key} has completed {value}% of the task(s) assigned to them.")

        for key,value in no_percent2.items():  # percentage of tasks the user has not completed
            uo.write(f"\n{key} has not completed {value}% of the task(s) asssigned to them.")

        for key,value in late_percent2.items():
            uo.write(f"\n{value}% of {key}'s tasks are incomplete and overdue.")

    print("Updated reports have been successfully generated.")

def display_stats():
    option = int(input('''Would you like to view the Tasks Overview report, or the User Overview report: 
                    1. Tasks
                    2. Users'''))

    if option == 1:
        with open("task_overview.txt", 'r') as stats:
            for lines in stats.readlines():
                print(lines)
                print('')

        option2 = int(input("Would you like to view the User Overview report?  1.Yes   2.No : "))

        if option2 == 1:
            with open("user_overview.txt", 'r') as stats2:
                for lines in stats2.readlines():
                    print(lines)

        elif option2 == 2:
            pass

        else:
            pass

    elif option == 2:
        with open("user_overview.txt", 'r') as stats1:
            for lines in stats1.readlines():
                print(lines)
                print('')

        option2 = int(input("Would you like to view the Task Overview report?  1.Yes   2.No : "))

        if option2 == 1:
            with open("task_overview.txt", 'r') as stats2:
                for lines in stats2.readlines():
                    print(lines)

        elif option2 == 2:
            pass

        else:
            pass

# Entering your log in information
while logged_in == False:
    data = user_data()

    name = input("Enter your username: ")
    word = input("Enter your password: ")

    if name not in data.keys():
        print("This username does not exist.")  # failed username log in
        logged_in = False

    elif word != data[name]:
        print("Incorrect password. Please try again")  # failed password login
        logged_in = False

    else:
        print(f"Access granted. Welcome, {name}.")  # successful login
        logged_in = True

if name == 'admin':
    admin_logged = True  # admin is logged in

# When successfully logged in
while logged_in == True or admin_logged == True:
    print("")
    option = input('''Please select one of the following options:
    r  -    register a user
    a  -    add a task
    va -    view all tasks
    vm -    view my tasks
    gr -    generate reports
    ds -    display statistics
    e  -    exit
          ''').lower()  # to ensure we get an acceptable input

    # Registering a user
    if option == 'r':

        if name == "admin":
            reg_user()
        else:
            admin_logged = False

        # if admin is not logged in and a user tries to access certain features
        while admin_logged == False:
            print("Only 'admin' has access to this feature.")
            break
            logged_in = True  # take user back to menu


    # Adding a task
    elif option == 'a':
        task_add()

    # Viewing all tasks
    elif option == 'va':
        view_all()

    # viewing your tasks
    elif option == 'vm':
        view_mine()

    elif option == 'gr':
        generate()

    # Exiting the program
    elif option == 'e':
        print(f"Goodbye {name}.")
        exit()

    # Displaying stats
    elif option == 'ds':
        if name == "admin":
            admin_logged = True

            if admin_logged:
                display_stats()


        else:
            # if admin is not logged in and a user tries to access certain features
            while admin_logged == False:
                print("Only 'admin' has access to this feature.")
                break
                admin_logged = False
                logged_in = True  # take user back to menu


