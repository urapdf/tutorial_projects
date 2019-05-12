import datetime


# noinspection PyPep8,PyPep8
def test_get_records_v(db):
    """

    :param db:
    :return:
    """
    #This Works sqllite search

    cursor = db.execute_sql("select * from Worklog WHERE date_of_task BETWEEN '2017/12/07' AND '2017/12/08';")

    for row in cursor.fetchall():
        print (row)

    cursor = db.execute_sql('select count(*) from Worklog;')
    res = cursor.fetchone()
    print ('Total: ', res[0])



def test_search(Worklog):

    """

    :param Worklog:
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
        print("Sorry, Nothing was found")


# noinspection PyPep8,PyPep8,PyPep8
def test_get_sqlite_query_between_2_dates(db):


    cursor = db.execute_sql("select * from Worklog WHERE date_of_task BETWEEN '2017/12/05' AND '2017/12/06';")

    for row in cursor.fetchall():
        print (row)

    cursor = db.execute_sql('select count(*) from Worklog;')
    res = cursor.fetchone()
    print ('Total: ', res[0])


# noinspection PyPep8Naming,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
def test_you_guys_are_insane(Worklog):

    #https://media.readthedocs.org/pdf/peewee/latest/peewee.pdf

    """

    :param Worklog:
    """
    print('bye')


    start_date = datetime.date(2016,1,1)
    end_date = datetime.date(2017,1,4)

    query = Worklog.select().where((Worklog.date_of_task > start_date) & (Worklog.date_of_task  < end_date))
    for person in query:
        print(person)

#https://stackoverflow.com/questions/32342758/why-changing-datefield-formats-in-python-peewee-makes-queries-go-wrong
"""
You guys are insane. If you took one second to read the docs you wouldn't waste time posting these elaborate questions on SO.

SQLite stores dates as strings. Strings are sorted byte-wise. Using a format other than %Y-%m-%d will not sort the dates correctly.

So with SQLite, always store your dates as always store your dates as %Y-%m-%d  (which is the peewee default anyways).
"""


# noinspection PyPep8,PyPep8,PyPep8
def test_get_sqlite_query_exact_date_search(db,look_for_date):

    """

    :param db:
    :param look_for_date:
    """
    query_str = "select * from Worklog WHERE date_of_task IS '{}';".format(look_for_date)
    cursor = db.execute_sql(query_str)
    #cursor = db.execute_sql("select * from Worklog WHERE date_of_task IS '2017/12/06';")

    for row in cursor.fetchall():
        print (row)

    cursor = db.execute_sql('select count(*) from Worklog;')
    res = cursor.fetchone()
    print ('Total: ', res[0])


# noinspection PyPep8,PyPep8,PyPep8
def test_get_sqlite_query_time_search(db,look_for_time):

    """

    :param db:
    :param look_for_time:
    """
    query_str = "select * from Worklog WHERE duration_of_task IS '{}';".format(look_for_time)
    #cursor = db.execute_sql(query_str)
    cursor = db.execute_sql("select * from Worklog WHERE duration_of_task = '00:29';")

    for row in cursor.fetchall():
        print (row)

    cursor = db.execute_sql('select count(*) from Worklog;')
    res = cursor.fetchone()
    print ('Total: ', res[0])


# noinspection PyPep8,PyPep8,PyPep8
def test_get_sqlite_query_row_number(db,row_num):

    """

    :param db:
    :param row_num:
    """
    cur = db.execute_sql("select * from Worklog")
    col_name_list = [tup[0] for tup in cur.description]
    print(col_name_list)

    # query_str = "select * from Worklog WHERE id = '{}';".format(row_num)
    query_str = "DELETE from Worklog WHERE id = '{}';".format(row_num)
    cursor = db.execute_sql(query_str)
    # cursor = db.execute_sql("select * from Worklog WHERE id  = 1;")

    for row in cursor.fetchall():
        print (row)

    cursor = db.execute_sql('select count(*) from Worklog;')
    res = cursor.fetchone()
    print ('Total: ', res[0])


# noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
def test_get_sqlite_query_pattern_search(db,pattern):

    """

    :param db:
    :param pattern:
    """
    query_str = "select * from Worklog WHERE additional_notes LIKE '%{}%' OR task_name LIKE '%{}%';".format(pattern,pattern)

    cursor = db.execute_sql(query_str)
    # cursor = db.execute_sql("select * from Worklog WHERE additional_notes LIKE '%hel%';")
    # cursor = db.execute_sql("select * from Worklog WHERE additional_notes LIKE '%p%'OR task_name LIKE '%hel%';")
    for row in cursor.fetchall():
        print (row)

    cursor = db.execute_sql('select count(*) from Worklog;')
    res = cursor.fetchone()
    print ('Total: ', res[0])


# noinspection PyProtectedMember,PyPep8Naming
def test_print_all_logs(Worklog):

    """

    :param Worklog:
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
