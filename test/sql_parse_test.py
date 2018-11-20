import sql_meta_parse


# fields = sql_meta_parse.get_query_columns("select case when p > 0 then 1 else 0 end as cs from c where g > f")
#
#
# print(fields)


# fields = sql_meta_parse.get_query_columns("select COUNT(case when p > 0 then h else 0 end) as cs from c where g > f")
#
#
# print(fields)


fields = sql_meta_parse.get_query_columns("select if(a is not null, c, d) where g > f")


print(fields)