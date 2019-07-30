from unittest import TestCase

from data_analysis_framework import table_view


class TestTableView(TestCase):
    tv = table_view.TableView()
    tv.load("../config/features.json")


    def test_sub_query(self):

        sql = self.tv.sql_gen(["open_date", "first_trd_date"])
        print(sql)

    def test_sub_query(self):
        sql = self.tv.sql_gen(["last_trd_date", "first_trd_date"])
        print(sql)

    def test_query_all(self):
        sql = self.tv.sql_gen_all()
        print(sql)