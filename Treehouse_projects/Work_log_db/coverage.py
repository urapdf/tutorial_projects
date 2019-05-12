import unittest
import os
import menus_objects


class WorkLogsTests(unittest.TestCase):
    test_mm = menus_objects.Menus

    def setUp(self):
        pass

    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_if_db_exists(self):
        assert os.path.isfile("worklog.db")

    def test_get_sqlite_query_pattern_search(self):

        test_query_str = self.test_mm.get_sqlite_query_pattern_search(pattern_search='mil')
        assert type(test_query_str) is str

    def test_get_sqlite_query_time_of_project(self):

        test_query_str = self.test_mm.get_sqlite_query_time_of_project(look_for_time='00:30')
        assert type(test_query_str) is str

    def test_get_sqlite_query_worker_name(self):

        test_query_str = self.test_mm.get_sqlite_query_worker_name(worker_name='Jeff')
        assert type(test_query_str) is str

    def test_get_sqlite_query_task_name(self):

        test_query_str = self.test_mm.get_sqlite_query_task_name(task_name='Feed cats')
        assert type(test_query_str) is str

    def test_get_sqlite_query_exact_date_search(self):

        test_query_str = self.test_mm.get_sqlite_query_exact_date_search(look_for_date='2017/12/05')
        assert type(test_query_str) is str

    def test_main_menu(self):

        try:
            test_query_str = self.test_mm.main_menu(self, test_input='e')
            # print (test_query_str)
        except AttributeError:
            pass

    def test_search_menu(self):

        try:
            test_query_str = self.test_mm.search_menu(self, test_input='e')
            # print (test_query_str)
        except AttributeError:
            pass


if __name__ == '__main__':
    unittest.main()
