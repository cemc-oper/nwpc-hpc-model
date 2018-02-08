import sys
import os

from nwpc_hpc_model.workload_scheme.query_item import QueryItem


class QueryModel(object):
    def __init__(self):
        self.items = list()
        self.category_list = None

    def to_dict(self):
        result = dict()
        result['items'] = []
        for item in self.items:
            result['items'].append(item.to_dict())
        return result

    def set_category_list(self, category_list):
        self.category_list = category_list

    @staticmethod
    def build_from_category_list(record, category_list):
        lines = record
        model = QueryModel()

        if lines[0].startswith('llq: There is currently no job status to report.'):
            # not jobs
            return model

        if lines[0].startswith('llq:'):
            print('failure detected:', lines)
            return None
        if len(lines) < 3:
            print('unsupported output:', lines)
            return None

        summary_line = lines[-2]

        record_start_line_no_list = list()

        for i in range(0, len(lines) - 3):
            if lines[i].startswith("====="):
                record_start_line_no_list.append(i)
        record_start_line_no_list.append(len(lines)-2)

        for record_no in range(0, len(record_start_line_no_list)-1):
            record_lines = lines[record_start_line_no_list[record_no]: record_start_line_no_list[record_no+1]]

            item = QueryItem.build_from_category_list(record_lines, category_list)

            model.items.append(item)

        return model
