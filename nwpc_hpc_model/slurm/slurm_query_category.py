# coding: utf-8
from nwpc_hpc_model.workload_scheme import QueryCategory, QueryCategoryList


class SlurmQueryCategoryList(QueryCategoryList):

    def update_index_from_title_line(self, title_line):
        tokens = title_line.split()
        for index in range(0, len(tokens)):
            label = tokens[index]
            category = self.category_from_label(label)
            if category:
                category.record_parser_arguments = (index,)
                category.build_record_parser()
