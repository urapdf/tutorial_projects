"""
The CSV timesheets were a huge success but some more features are needed, including the ability for other
developers to use the data without worrying about file locking or availability.
The managers have also asked for a way to view time entries for each employee.
Seems like a database would be a better solution than a CSV file!

Create a command line application that will allow employees to enter their name, time worked, task worked on,
and general notes about the task into a database. There should be a way to add a new entry, list all entries for
a particular employee, and list all entries that match a date or search term. Print a report of this information
to the screen, including the date, title of task, time spent, employee, and general notes

As a fellow developer, I should find at least 50% of the code covered by tests. I would use coverage.py
to validate this amount of coverage.

http://docs.peewee-orm.com/en/latest/peewee/querying.html

"""
#imports
from peewee import *
import datetime
import os
import menus_objects
import prototype_functions
import sys


db = SqliteDatabase('worklog.db')


class Worklog(Model):

    worker_name = CharField(max_length=255, unique=False)
    task_name = CharField(max_length=255, unique=False)
    date_of_task = DateTimeField(default=datetime.datetime.now)
    duration_of_task = TimeField()
    additional_notes = CharField(max_length=255)

    class Meta:
        database = db

worklogs = [
    {"worker_name": "Thomas",
     "task_name": "Tutor",
     "date_of_task": "2017/05/20",
     "duration_of_task": "1d",
     "additional_notes": "No"},
    {"worker_name": "JeffII",
     "task_name": "Tutee",
     "date_of_task": "2016/06/01",
     "duration_of_task": "3d",
     "additional_notes": "Yes"}]


def add_single_row(entry_list):
    """
    :param entry_list:
    :return:
    """
    try:
        row = Worklog(
            worker_name=entry_list[0],
            task_name=entry_list[1],
            date_of_task=entry_list[2],
            duration_of_task=entry_list[3],
            additional_notes=entry_list[4]
        )

        row.save()
        mm.clear_screen()
    except TypeError:
        mm.clear_screen()
        print("Returning to main menu")


def add_work_logs(list_dict=worklogs):
    """
    add work logs from list

    :param list_dict:
    :return: None
    """
    for worklog in list_dict:
        try:
            Worklog.create(worker_name=worklog['worker_name'],
                           task_name=worklog['task_name'],
                           date_of_task=worklog['date_of_task'],
                           duration_of_task=worklog['duration_of_task'],
                           additional_notes=worklog['additional_notes'])
        except IntegrityError:
            log_record = Worklog.get(worker_name=worklog['worker_name'])
            log_record.task_name = worklog['task_name']


def print_all_records():
    """
    :return:
    """

    for worklog in Worklog.select():

        print(worklog.duration_of_task)
        print(worklog.worker_name)
        print("")


def test_search():
    """
    :return:
    """

    try:

        for worklog in Worklog.select():

            print("===============")
            print("Item: {} ".format(worklog._get_pk_value()))
            print("Worker Name: {}".format(worklog.worker_name))
            print("Task Name: {}".format(worklog.task_name))
            print("Date of Task: {}".format(worklog.date_of_task))
            print("Duration of Task: {}".format(worklog.duration_of_task))
            print("Additional Notes: {}".format(worklog.additional_notes))
            print("===============\n")
    except:
        mm.clear_screen()
        print("Sorry, Nothing was found")


def print_specific_records(cursor, databass=db):
    """
    :param cursor:
    :param databass:
    :return:
    """
    print("\n This are the records we found\n")
    for row in cursor.fetchall():
        print(row[0], row[2], row[3], "\n")

    cursor_ii = databass.execute_sql('select count(*) from Worklog;')
    res = cursor_ii.fetchone()
    print('Total records in database: ', res[0])


def print_full_record(cursor):
    """
    :param cursor:
    :return:
    """
    print("===============")

    for row in cursor:
        print("Item: {} ".format(row[0]))
        print("Worker Name: {}".format(row[1]))
        print("Task Name: {}".format(row[2]))
        print("Date of Task: {}".format(row[3]))
        print("Duration of Task: {}".format(row[4]))
        print("Additional Notes: {}".format(row[5]))


def get_list_of_all_valid_rows(query_str='select * from Worklog where date_of_task IS NOT NULL'
                                         ' or  date_of_task = "";'):
    """
    :param query_str:
    :return:
    """

    list_of_valid_rows = []

    cursor = db.execute_sql(query_str)

    for row in cursor:
        list_of_valid_rows.append(row[0])

    return list_of_valid_rows


def browse_all_records(query_str='select * from Worklog where date_of_task IS NOT NULL'
                                 ' or  date_of_task = "";'):
    """
    :param query_str:
    :return:
    """
    current_row_index = 0

    list_of_valid_rows = get_list_of_all_valid_rows(query_str)

    if len(list_of_valid_rows) > 0:
        query_str = mm.get_sqlite_query_id_row(current_row_index, list_of_valid_rows)
        cursor = db.execute_sql(query_str)
        print("There are {} records that meet your query.\n"
              "Please browse through the entries\n".format(len(list_of_valid_rows)))
        print_full_record(cursor)
    else:
        print("Sorry, No records found")

    user_choice = ""
    while user_choice.upper() in ("P", "N", "") and len(list_of_valid_rows) > 0:
        user_choice = mm.scroll_menu_options()
        current_row_index = mm.change_row_position(list_of_valid_rows, user_choice, current_row_index)
        query_str = mm.get_sqlite_query_id_row(current_row_index, list_of_valid_rows)
        cursor = db.execute_sql(query_str)
        mm.clear_screen()
        print_full_record(cursor)

        if user_choice.upper() == "D":
            query_str = mm.get_sqlite_delete_record(list_of_valid_rows[current_row_index])
            db.execute_sql(query_str)


def search_menu():
    """
    :return:
    """
    mm.search_header()

    user_search_choice = ("", "")
    while user_search_choice[0].upper() != 'M':
        user_search_choice = mm.search_menu()
        cursor = db.execute_sql(user_search_choice[1])
        browse_all_records(user_search_choice[1])
        # print_specific_records(cursor)


if __name__ == '__main__':

    mm = menus_objects.Menus()

    if not os.path.isfile("worklog.db"):
        db.connect()
        db.create_tables([Worklog], safe=True)

    user_choice = ""
    while user_choice.upper() != "E":
        mm.work_header()
        print("What would you like to do? ")
        user_choice = input("A)dd new entry \n"
                            "S)earch in existing entries \n"
                            "B)rowse through existing entries \n"
                            "E)xit \n>")

        user_choice = user_choice.upper().strip()
        if user_choice.upper() == "A":
            entry = mm.add_new_entry()
            add_single_row(entry)

        elif user_choice.upper() == "S":
            mm.clear_screen()
            search_menu()

        elif user_choice.upper() == "B":
            mm.clear_screen()
            browse_all_records()
        elif user_choice.upper() == "T":
            pass
        elif user_choice.upper() != "E":
            print("Sorry, Don't understand. Please try again \n ")

        else:
            if user_choice.upper() == "E":
                print("Good bye")
                sys.exit(0)

    worklogsII = [
        {"worker_name": "MilkyIV",
         "task_name": "Feed_meIII",
         "date_of_task": "10/12/2017",
         "duration_of_task": "8d",
         "additional_notes": "Pig"}]

    # add_work_logs()
    # add_single_row(worklogsII[0]["worker_name"],worklogsII[0]["task_name"],worklogsII[0]["date_of_task"],
    #                worklogsII[0]["duration_of_task"],worklogsII[0]["additional_notes"])
    print_all_records()




