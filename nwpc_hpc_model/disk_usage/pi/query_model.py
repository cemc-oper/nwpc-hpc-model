# coding: utf-8
from nwpc_hpc_model.base.query_model import QueryModel
from nwpc_hpc_model.disk_usage.pi import QueryItem


class PiDiskUsageQueryModel(QueryModel):
    def __init__(self):
        QueryModel.__init__(self)

    @classmethod
    def build_from_category_list(cls, record, category_list):
        if len(record) == 0:
            return None
        user_line = record[0]
        title_line = record[1]
        lines = record[2:]
        model = PiDiskUsageQueryModel()

        for line in lines:
            if len(line) == 0:
                continue
            item = QueryItem.build_from_category_list(line, category_list)
            model.items.append(item)

        return model
