from unittest import TestCase

from data_analysis_framework import group_analysis


class TestGroupAnalysis(TestCase):
    def test_distribution(self):
        gs = group_analysis.GroupAnalysis("../config/features.json")
        sql = gs \
            .distribution("trd_days")

        print(sql)
