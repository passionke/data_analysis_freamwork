from data_analysis_framework import config


class TableView:
    i = 0

    cfg = None

    def load(self, path):
        cfg = config.Config()
        cfg.load(path)
        self.cfg = cfg

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

    def sql_gen(self, dims, extra_dim=None):
        main_dim = dims[0]
        pre_dependency = "\n".join(map(lambda x: "--@extra_input=adm_ddm_app_mct_smdc_pid_index_ds_" + str(x), dims))
        groups = map(lambda dim: self.group(self.cfg.table, dim), dims[1:])
        if extra_dim is not None:
            raw_sql = "select " + ",\n".join(dims) + " , " + extra_dim + " \n from " + self.sub_query(self.cfg.table,
                                                                                                      main_dim) + " \n ".join(
                groups)
        else:
            raw_sql = "select " + ",\n".join(dims) + " \n from " + self.sub_query(self.cfg.table,
                                                                                  main_dim) + " \n ".join(
                groups)
        return pre_dependency + "\n" + raw_sql

    def sql_gen_all(self):
        return self.sql_gen(list(self.cfg.fields.keys()))
