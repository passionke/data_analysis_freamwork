from data_analysis_framework import sql_meta_parse
from data_analysis_framework import table_view
from data_analysis_framework import formatter


class GroupAnalysis:
    filter_expressions = set()
    filter_expressions.add("true")
    view = None
    table_view = table_view.TableView()

    def __init__(self, path):
        self.table_view.load(path)

    def where(self, filter_exp):
        self.filter_expressions.add(filter_exp)
        return self

    def statistics(self, dim):
        if " as " not in str(dim).lower():
            sql = self.build_pre_sql(dim)
            columns = sql_meta_parse.get_query_columns(sql)
            from_sql = self.table_view.sql_gen(columns)
            pre_dependency = "\n".join(map(lambda x: "--@extra_input=adm_ddm_app_mct_smdc_pid_index_ds_"+ str(x), columns))
            final_sql = self.build_statstics_sql(dim, from_sql)
            pretty_sql = formatter.format_sql(pre_dependency + "\n" + final_sql)
            return pretty_sql
        else:
            sql = self.build_pre_sql(dim)
            columns = sql_meta_parse.get_query_columns(sql)
            from_sql = self.table_view.sql_gen(columns, dim)
            real_dim = str(dim).lower().split(" as ")[1]
            final_sql = self.build_statstics_sql(real_dim, from_sql)
            pretty_sql = formatter.format_sql(final_sql)
            return pretty_sql

    def distribution(self, dim):
        if " as " not in str(dim).lower():
            sql = self.build_pre_sql(dim)
            columns = sql_meta_parse.get_query_columns(sql)
            from_sql = self.table_view.sql_gen(columns)
            pre_dependency = "\n".join(map(lambda x: "--@extra_input=adm_ddm_app_mct_smdc_pid_index_ds_"+ str(x), columns))
            final_sql = self.build_final_sql(dim, from_sql)
            pretty_sql = formatter.format_sql(pre_dependency + "\n" + final_sql)
            return pretty_sql
        else:
            sql = self.build_pre_sql(dim)
            columns = sql_meta_parse.get_query_columns(sql)
            from_sql = self.table_view.sql_gen(columns, dim)
            real_dim = str(dim).lower().split(" as ")[1]
            final_sql = self.build_final_sql(real_dim, from_sql)
            pretty_sql = formatter.format_sql(final_sql)
            return pretty_sql

    def build_pre_sql(self, dim):
        statement = ["SELECT", dim, "FROM placeHolder", "WHERE",
                     " and ".join(self.filter_expressions)]
        return "\n".join(list(statement))

    def build_final_sql(self, dim, sub_query):
        statement = ["SELECT ", dim, ", ", "count(1) as cnt ", "FROM (" , sub_query,
                     " where ",
                     " and ".join(self.filter_expressions), ") a", "group by " + dim]
        sub = "\n".join(statement)
        statement = ["select", ",".join([dim, "cnt", "sum(cnt) over() as total ", "rate_4(cnt, sum(cnt) over()) as percent"]), "from (", sub, ") a"]
        return "\n".join(statement)

    def build_statstics_sql(self, dim, sub_query):
        statement = ["SELECT ", "avg(" + dim + ") as mean_" + dim ,
                     ","
                     "max(" + dim + ") as max_" + dim,
                     ","
                     "percentile(" + dim + ", array(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)) as percent_" + dim,
                     "FROM (" , sub_query,
                     " where ",
                     " and ".join(self.filter_expressions), ") a"]
        return "\n".join(statement)


