import datetime
import re
import os
import sys

def work_header():
    print("===============")
    print("    Work Log   ")
    print("=============== \n")


def main_menu():
    user_choice = ""
    while user_choice.upper() != "E":
        work_header()
        print("What would you like to do? ")
        user_choice = input("A)dd new entry \n"
                            "S)earch in existing entries \n"
                            "B)rowse through existing entries \n"
                            "E)xit \n>")
        user_choice = user_choice.upper().strip()
        if user_choice.upper() == "A":
            add_new_entry()
        elif user_choice.upper() == "S":
            clear_screen()
            search_menu()
        elif user_choice.upper() == "B":
            clear_screen()
            scroll_entries()
        elif user_choice.upper() != "E":
            print("Sorry, Don't understand. Please try again \n ")

        else:
            if user_choice.upper() == "E":
                print("Good bye")
                sys.exit(0)


def add_new_entry():
    work_order_list = [None, None, None, None]
    clear_screen()
    print("Enter 'EXIT' to return to main menu")
    work_order_list[0] = input("Name of work order? > ")
    if work_order_list[0].upper() == "EXIT":
        main_menu()

    clear_screen()
    work_order_list[1] = get_user_date()
    if work_order_list[1] == "EXIT":
        main_menu()
    clear_screen()
    work_order_list[2] = get_user_time()
    if work_order_list[2] == "EXIT":
        main_menu()
    work_order_list[3] = input("Add any notes > ")
    if work_order_list[3] == "EXIT":
        main_menu()

    add_to_log_file(work_order_list)


def search_menu():
    search_choice = ""
    clear_screen()
    while search_choice.upper() != 'M':
        print("How would you want to search?\n ")
        search_choice = input("E)xact date \n"
                              "D)ate range   \n"
                              "N)ame of work order  \n"
                              "R)egex pattern \n"
                              "T)ime spent on project \n"
                              "M)ain menu \n"
                              "> ")
        search_choice = search_choice.lower().strip()
        if search_choice == 'g':
            test_search()
        elif search_choice.upper() == 'E':
            look_for_date = get_user_date()
            exact_date_search(look_for_date)
        elif search_choice.upper() == 'D':
            start_date = get_user_date("initial ")
            end_date = get_user_date("end ")
            search_csv_date_range(start_date, end_date)
        elif search_choice.upper() == 'N':
            search_via_exact_name()
        elif search_choice.upper() == 'R':
            search_via_regex()
        elif search_choice.upper() == 'T':
            user_time_spent = get_user_time()
            search_via_time_spent(user_time_spent)


def get_user_date(date_type=""):
    date_format = '%m/%d/%Y'
    menu_loop = True

    while menu_loop:

        user_date = input("Please enter {}work order date (mm/dd/yyyy)\n "
                          "or 'EXIT' to go back to main menu > ".format(date_type))
        if user_date.upper() == 'EXIT':
            menu_loop = False
            main_menu()

        try:
            work_date = datetime.datetime.strptime(user_date, date_format).strftime(date_format)
            return work_date
        except ValueError:
            print("Wrong format...")
    menu_loop = False


def get_user_time():
    time_format = '%H:%M'
    minperhour = 60

    while True:
        user_time = input("Please enter time spent in minutes \n or 'EXIT' to go back to main menu > ")
        if user_time.upper() == 'EXIT':
            main_menu()
        try:
            user_hours = int(user_time) // minperhour
            user_mins = int(user_time) % minperhour
            work_time = datetime.time(user_hours, user_mins).strftime(time_format)
            return work_time
        except ValueError:
            print("Wrong format...please enter minutes as a whole number > ")


def add_to_log_file(work_order):
    work_logfile = "worklog.csv"
    with open(work_logfile, 'a') as f:
        f.write(','.join(work_order) + '\n')


def exact_date_search(look_for_date):

    try:
        for i, line in enumerate(open('worklog.csv', 'r')):
            csv_row = line.split(",")
            if look_for_date == csv_row[1]:
                print_work_order(csv_row, i)
    except:
        clear_screen()
        no_records_found()


def test_search():

    try:

        for i, line in enumerate(open('worklog.csv','r')):
            csv_row = line.split(",")

            print("===============")
            print("Row: ", i)
            print("Work Order: {}".format(csv_row[0]))
            print("Work Date: {}".format(csv_row[1]))
            print("Work Time: {}".format(csv_row[2]))
            print("Work Notes: {}".format(csv_row[3]))
            print("===============\n")
    except:
        clear_screen()
        print("Sorry, Nothing was found")


def print_work_order(csv_row, work_order_num):

        print("===============")
        print ("Row: ", work_order_num)
        print("Work Order: {}".format(csv_row[0]))
        print("Work Date: {}".format(csv_row[1]))
        print("Work Time: {}".format(csv_row[2]))
        print("Work Notes: {}".format(csv_row[3]))
        print("===============\n")


def search_csv_date_range(start_date, end_date):
    does_file_exists('worklog.csv')
    records_found = None
    date_format = '%m/%d/%Y'
    start_date = datetime.datetime.strptime(start_date, date_format)
    end_date = datetime.datetime.strptime(end_date, date_format)

    for i, line in enumerate(open('worklog.csv', 'r')):
        csv_row = line.split(",")
        csv_date = datetime.datetime.strptime(csv_row[1], date_format)
        if start_date <= csv_date and end_date >= csv_date:
            print_work_order(csv_row, i)
            records_found = True

        if records_found is None:
            no_records_found()


def verify_regex(user_input):
    # invalid case: '^*'+device+'@'
    # valid case: .*([1-3][0-9]{3})
    try:
        re.compile(user_input)
        is_valid = True
    except re.error:
        is_valid = False

    return is_valid


def search_via_regex():

    does_file_exists('worklog.csv')
    records_found = None
    user_query = input("Please enter regex expression\n > ")
    if verify_regex(user_query):
        for i, line in enumerate(open('worklog.csv', 'r')):
            if re.match(user_query, line):
                print_work_order(line.split(","), i)
                records_found = True
        if records_found is None:
            no_records_found()
    else:
        print("entered invalid regular expression")


def search_via_exact_name():
    does_file_exists('worklog.csv')
    look_for_order_name = input("Please enter order name you want to search for\n >").strip()
    records_found = None

    while look_for_order_name != "EXIT":
        for i, line in enumerate(open('worklog.csv', 'r')):
            csv_row = line.split(",")
            if look_for_order_name == csv_row[0]:
                records_found = True
                print_work_order(csv_row, i)
        if records_found is None:
            no_records_found()

        look_for_order_name = input("Please enter order name you want to search for"
                                    " or 'EXIT' to go to main menu\n > ").strip()


def search_via_time_spent(user_time_spent):

    does_file_exists('worklog.csv')
    records_found = None

    for i, line in enumerate(open('worklog.csv', 'r')):
        csv_row = line.split(",")
        if user_time_spent == csv_row[2]:
            records_found = True
            print_work_order(csv_row, i)
    if records_found is None:
        no_records_found()


def scroll_entries():
    clear_screen()
    i = 0
    try:
        with open('worklog.csv', 'r') as worklog:
            csv_row = worklog.readline().split(",")
            print_work_order(csv_row, i)
            idx_list = [0]
            for idx, row in enumerate(worklog):
                idx_list.append(idx + 1)
    except:
        clear_screen()
        print("Sorry, No work entries exist, please add some")
        main_menu()

    user_choice = scroll_menu_options()
    while user_choice.upper() != "E" or user_choice.upper() != "D":
        if user_choice.upper() == "P":
            i -= 1
            if abs(i) > len(idx_list):
                i =- 1
        elif user_choice.upper() == "N":
            i += 1
            if i >= len(idx_list):
                i = 0
        elif user_choice.upper() == "D":
            delete_work_entry(i)


        clear_screen()
        with open('worklog.csv', 'r') as worklog:
            for idx, row in enumerate(worklog):
                if idx == idx_list[i]:
                    print_work_order(row.split(","), idx)

        if user_choice.upper() == "E":
            main_menu()
        elif user_choice.upper() != "D":
            user_choice = scroll_menu_options()
        else:
            delete_work_entry(i)


def scroll_menu_options():
    return input("P)revious N)ext D)elete or E)xit\n>" )


def delete_work_entry(work_order_row):
    user_confirm = input("Are you sure you want to delete this entry?(Y/N)\n> ")
    if user_confirm.upper() == 'Y':
        with open('worklog.csv', 'r') as worklog:
            with open('worklog_new.csv', 'w') as worklog_new:
                for idx, row in enumerate(worklog):
                    if idx != work_order_row:
                        worklog_new.write(row)
        os.remove('worklog.csv')
        os.rename('worklog_new.csv', 'worklog.csv')

    main_menu()


def clear_screen():
    print("\033c", end="")


def does_file_exists(filename):
    my_file =  os.path.isfile(filename)
    if not my_file:
        clear_screen()
        print("Sorry, There are no records. PLease add work logs before searching")
        main_menu()


def no_records_found():
    print("Sorry no records found, Please try again")


clear_screen()
main_menu()
