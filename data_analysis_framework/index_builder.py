import sql_meta_parse
from table_view import TableView
import sql_format


class IndexBuilder:
    filter_expressions = set()
    agg_expressions = set()
    view = None
    table_view = TableView()

    def __init__(self, path):
        self.table_view.load(path)

    def where(self, filter_exp):
        self.filter_expressions.add(filter_exp)
        return self

    def agg(self, agg_exp):
        self.agg_expressions.add(agg_exp)
        return self

    def build_pre_sql(self):
        statement = ["SELECT", ",".join(self.agg_expressions), "FROM placeHolder", "WHERE",
                     " and ".join(self.filter_expressions)]
        return "\n".join(list(statement))

    def build_final_sql(self, sub_query):
        statement = ["SELECT", ",".join(self.agg_expressions), "FROM (", sub_query, ") a", "WHERE",
                     " and ".join(self.filter_expressions)]
        return "\n".join(list(statement))

    def execute(self):
        sql = self.build_pre_sql()
        columns = sql_meta_parse.get_query_columns(sql)
        from_sql = self.table_view.sql_gen(columns)
        final_sql = self.build_final_sql(from_sql)
        pretty_sql = sql_format.format(final_sql)
        return pretty_sql

