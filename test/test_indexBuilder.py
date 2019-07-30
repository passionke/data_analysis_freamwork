from unittest import TestCase

from data_analysis_framework import index_builder


class TestIndexBuilder(TestCase):

    def test(self):
        ib = index_builder.IndexBuilder("../config/features.json")

        sql = ib.where("trd_success_cnt_1d > 0") \
            .group_by("province") \
            .agg(["count(1) as province_trd" ]) \
            .execute()
        print(sql)
