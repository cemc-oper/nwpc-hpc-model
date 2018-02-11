# coding=utf-8
from nwpc_hpc_model.workload import QueryModel, QueryItem


class SlurmQueryModel(QueryModel):
    def __init__(self):
        QueryModel.__init__(self)

    @classmethod
    def build_from_table_category_list(cls, record, category_list, sep=None):
        if len(record) == 0:
            return None

        title_line = record[0]
        category_list.update_index_for_table_query(title_line, sep)

        lines = record[1:]
        model = SlurmQueryModel()

        if len(lines) == 0:
            return model

        for line in lines:
            if len(line) == 0:
                continue
            item = QueryItem.build_from_category_list(line, category_list)
            model.items.append(item)

        return model
