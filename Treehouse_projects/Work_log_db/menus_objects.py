import datetime


class Menus(object):
    @staticmethod
    def work_header():
        """
        :return:
        """
        print("===============")
        print("    Work Log   ")
        print("=============== \n")

    @staticmethod
    def search_header():
        """
        :return:
        """
        print("===============")
        print("  Search Menu   ")
        print("=============== \n")

    @staticmethod
    def clear_screen():
        """
        :return:
        """
        print("\033c", end="")

    def main_menu(self, test_input=False):
        """
        :param test_input:
        :return:
        """
        if not test_input:
            user_choice = ""
            while user_choice.upper() != "E":
                self.work_header()
                print("What would you like to do? ")
                user_choice = input("A)dd new entry \n"
                                    "S)earch in existing entries \n"
                                    "B)rowse through existing entries \n"
                                    "E)xit \n>")
                user_choice = user_choice.upper().strip()
        else:
            user_choice = test_input

    def add_new_entry(self):
        """
        :return:
        """
        work_order_list = [None, None, None, None, None]

        self.clear_screen()
        print("Enter 'EXIT' to return to main menu")
        work_order_list[0] = input("Name of worker? > ")
        if work_order_list[0].upper() == "EXIT":
            return 0

        work_order_list[4] = input("Name of task? > ")
        if work_order_list[4] == "EXIT":
            return 0
        work_order_list[1] = self.get_user_date()
        if work_order_list[1] == "EXIT":
            return 0
        work_order_list[2] = self.get_user_time()
        if work_order_list[2] == "EXIT":
            return 0
        work_order_list[3] = input("Add any notes > ")
        if work_order_list[3] == "EXIT":
            return 0

        work_order_list = [work_order_list[0]] + \
                          [work_order_list[4]] + \
                          [work_order_list[1]] + \
                          [work_order_list[2]] +\
                          [work_order_list[3]]
        return work_order_list

    @staticmethod
    def get_user_date(date_type=""):
        """
        :param date_type:
        :return:
        """
        date_format = '%Y/%m/%d'
        menu_loop = True

        while menu_loop:

            user_date = input("Please enter {}work order date (Y/m/d)\n "
                              "or 'EXIT' to go back to main menu > ".format(date_type))
            if user_date.upper() == 'EXIT':
                menu_loop = False
                return "EXIT"

            try:
                work_date = datetime.datetime.strptime(user_date, date_format).strftime(date_format)
                return work_date
            except ValueError:
                print("Wrong format...")

    @staticmethod
    def get_user_time():
        """
        :return:
        """
        time_format = '%H:%M'
        minperhour = 60

        while True:
            user_time = input("Please enter time spent in minutes \n or 'EXIT' to go back to main menu > ")
            if user_time.upper() == 'EXIT':
                return "EXIT"
            try:
                user_hours = int(user_time) // minperhour
                user_mins = int(user_time) % minperhour
                work_time = datetime.time(user_hours, user_mins).strftime(time_format)
                return work_time
            except ValueError:
                print("Wrong format...please enter minutes as a whole number > ")

    @staticmethod
    def get_sqlite_delete_record(current_row_index):
        """
        :param current_row_index:
        :return:
        """

        query_str = "DELETE from Worklog WHERE id = '{}';".format(current_row_index)

        return query_str

    @staticmethod
    def get_sqlite_query_exact_date_search(look_for_date):
        """
        :param look_for_date:
        :return:
        """

        query_str = "select * from Worklog WHERE date_of_task = '{}';".format(look_for_date)

        return query_str

    @staticmethod
    def get_sqlite_query_time_of_project(look_for_time):
        """
        :param look_for_time:
        :return:
        """

        query_str = "select * from Worklog WHERE duration_of_task IS '{}';".format(look_for_time)

        return query_str

    @staticmethod
    def get_sqlite_query_worker_name(worker_name):
        """
        :param worker_name:
        :return:
        """

        query_str = "select * from Worklog WHERE worker_name IS '{}';".format(worker_name)

        return query_str

    @staticmethod
    def get_sqlite_query_task_name(task_name):
        """
        :param task_name:
        :return:
        """

        query_str = "select * from Worklog WHERE task_name IS '{}';".format(task_name)

        return query_str

    @staticmethod
    def get_sqlite_query_date_range(start_date, end_date):

        query_str = "select * from Worklog WHERE date_of_task BETWEEN '{}'AND '{}';".format(start_date, end_date)

        return query_str

    @staticmethod
    def get_sqlite_query_pattern_search(pattern_search):
        """
        :param pattern_search:
        :return: sql formated string
        """

        query_str = "select * from Worklog WHERE additional_notes LIKE '%{}%'" \
                    " OR task_name LIKE '%{}%';".format(pattern_search, pattern_search)

        return query_str

    def search_menu(self, test_input=False):
        """
        :param test_input:
        :return:
        """

        # self.clear_screen()

        if not test_input:
            print("How would you want to search?\n ")
            search_choice = input("E)xact date \n"
                                  "D)ate range   \n"
                                  "W)orker name \n"
                                  "N)ame of work order  \n"
                                  "P)attern \n"
                                  "T)ime spent on project \n"
                                  "M)ain menu \n"
                                  "> ").upper().strip()
        else:
            search_choice = test_input

        while search_choice or search_choice == "":
            if search_choice == 'M':
                self.clear_screen()
                return search_choice, ""
            elif search_choice.upper() == 'E':
                look_for_date = self.get_user_date()
                query_str = self.get_sqlite_query_exact_date_search(look_for_date)
                return search_choice, query_str
            elif search_choice.upper() == 'W':
                worker_name = input("Enter the name of the worker you want to search:")
                query_str = self.get_sqlite_query_worker_name(worker_name)
                return search_choice, query_str
            elif search_choice.upper() == 'D':
                start_date = self.get_user_date()
                end_date = self.get_user_date()
                query_str = self.get_sqlite_query_date_range(start_date, end_date)
                return search_choice, query_str
            elif search_choice.upper() == 'N':
                task_name = input("Enter the name of task you want to search:")
                query_str = self.get_sqlite_query_task_name(task_name)
                return search_choice, query_str
            elif search_choice.upper() == 'P':
                pattern_search = input("Enter your search pattern:")
                query_str = self.get_sqlite_query_pattern_search(pattern_search)
                return search_choice, query_str
            elif search_choice.upper() == 'T':
                look_for_time = self.get_user_time()
                query_str = self.get_sqlite_query_time_of_project(look_for_time)
                return search_choice, query_str
            else:
                search_choice = input("Please enter valid choice:").upper().strip()

    @staticmethod
    def get_sqlite_query_id_row(current_row_index, list_of_valid_rows):
        """
        :param current_row_index:
        :param list_of_valid_rows:
        :return:
        """

        query_str = "select * from Worklog WHERE id  = '{}';".format(list_of_valid_rows[current_row_index])

        return query_str

    @staticmethod
    def change_row_position(list_of_valid_rows, user_choice, current_row_index):
        """
        :param list_of_valid_rows:
        :param user_choice:
        :param current_row_index:
        :return:
        """

        if user_choice.upper() == "P":
            current_row_index -= 1
            if abs(current_row_index) > len(list_of_valid_rows):
                current_row_index -= 1
        elif user_choice.upper() == "N":
            current_row_index += 1
            if current_row_index >= len(list_of_valid_rows):
                current_row_index = 0

        return current_row_index

    @staticmethod
    def scroll_menu_options():
        """
        :return: input string of valid choices
        """
        return input("\nP)revious N)ext D)elete or E)xit\n>")
