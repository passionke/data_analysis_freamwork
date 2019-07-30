from unittest import TestCase

from data_analysis_framework import group_analysis


class TestGroupAnalysis(TestCase):
    def test_distribution(self):
        gs = group_analysis.GroupAnalysis("../config/features.json")
        sql = gs \
            .distribution("trd_days")

        print(sql)

    def test_distribution1(self):
        gs = group_analysis.GroupAnalysis("../config/features.json")
        sql = gs \
            .distribution("DATEDIFF(first_trd_date, open_date, 'dd') as after_days")
        print(sql)

    def test_used_smdc_trd_cnt_7d_dist(self):
        gs = group_analysis.GroupAnalysis("../config/features.json")
        sql = gs \
            .where("used_smdc_trd_cnt_7d >0") \
            .where("buy_qr_materiel = 1") \
            .distribution("used_smdc_trd_cnt_7d")
        print(sql)

    def test_used_smdc_trd_cnt_7d_stastics(self):
        gs = group_analysis.GroupAnalysis("../config/features.json")
        sql = gs \
            .where("used_smdc_trd_cnt_1d >0") \
            .where("buy_qr_materiel = 1") \
            .statistics("used_smdc_trd_cnt_1d")
        print(sql)

    def test_trd_provice(self):
        gs = group_analysis.GroupAnalysis("../config/features.json")
        sql = gs \
            .where("used_smdc_trd_cnt_1d > 0") \
            .distribution("province")

        print(sql)