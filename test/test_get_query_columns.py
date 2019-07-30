from unittest import TestCase
from data_analysis_framework import sql_meta_parse


class TestGet_query_columns(TestCase):
    def test_get_query_columns(self):
        f = sql_meta_parse.get_query_columns("select a as b from d")
        print(f)
