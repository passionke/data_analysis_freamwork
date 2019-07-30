from data_analysis_framework import sql_meta_parse


# fields = sql_meta_parse.get_query_columns("select case when p > 0 then 1 else 0 end as cs from c where g > f")
#
#
# print(fields)


# fields = sql_meta_parse.get_query_columns("select COUNT(case when p > 0 then h else 0 end) as cs from c where g > f")
#
#
# print(fields)


fields = sql_meta_parse.get_query_columns("""
SELECT
used_smdc_trd_cnt_7d
FROM placeHolder
WHERE
true and buy_qr_materiel = 1 and used_smdc_trd_cnt_7d is not null
""")


print(fields)