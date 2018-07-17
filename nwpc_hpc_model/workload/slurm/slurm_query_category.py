# coding: utf-8
from nwpc_hpc_model.base.query_category import QueryCategoryList


class SlurmQueryCategoryList(QueryCategoryList):

    def update_index_for_table_query(self, title_line, sep=None):
        title_line = title_line.strip()
        if sep is None:
            tokens = title_line.split()
        else:
            tokens = title_line.split('|')
        for index in range(0, len(tokens)):
            label = tokens[index]
            category = self.category_from_label(label)
            if category:
                category.record_parser_arguments = (index, sep)
                category.build_record_parser()
