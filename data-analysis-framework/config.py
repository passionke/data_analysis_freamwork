import json


class Config:
    table = ""
    fields = []
    join_key = ""

    def load(self, path):
        with open(path) as json_data:
            d = json.load(json_data)
            self.table = d["table_name"]
            self.fields = d["index_key_list"]
            self.join_key = d["join_key"]
