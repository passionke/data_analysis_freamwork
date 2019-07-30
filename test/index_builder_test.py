
from data_analysis_framework import index_builder

ib = index_builder.IndexBuilder("../config/features.json")

sql = ib.where("smdc_trd_cnt_1d > 0")\
    .agg(["count(case when has_bind_qrcode = 1 then 1 end) as qr_cnt",
          "count(case when has_bind_qrcode = 0 then 1 end) as qr_cnt1"]) \
    .execute()


print(sql)