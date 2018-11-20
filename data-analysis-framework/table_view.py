from config import Config


class TableView:
    i = 0

    cfg = None

    def load(self, path):
        config = Config()
        config.load(path)
        self.cfg = config

    def get_type(self, dim):
        if dim in self.cfg.fields:
            return self.cfg.fields[dim]
        else:
            raise RuntimeError(dim + " not exist in " + self.cfg.table)

    def sub_query(self, table, dim):
        return "(SELECT " + self.cfg.join_key + ", cast(value as " + self.get_type(
            dim) + ") as " + dim + " FROM    " + table + " WHERE   dt = '${bizdate}'  AND  index_key = \"" + dim + \
               "\") t_" + str(
            self.i) + " \n"

    def group(self, table, dim):
        self.i = self.i + 1
        sql = "LEFT OUTER JOIN  " + self.sub_query(table, dim) + " ON t_0." + self.cfg.join_key + " = t_" + \
              str(self.i) + "." + self.cfg.join_key
        return sql

    def sql_gen(self, dims):
        main_dim = dims[0]
        groups = map(lambda dim: self.group(self.cfg.table, dim), dims[1:])
        raw_sql = "select " + ",\n".join(dims) + " \n from " + self.sub_query(self.cfg.table, main_dim) + " \n ".join(
            groups)
        return raw_sql
