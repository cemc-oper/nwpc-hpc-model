# coding: utf-8
from nwpc_hpc_model.base.query_category import QueryCategoryList, QueryCategory
from . import record_parser, value_saver


class PiDiskSpaceCategoryList(QueryCategoryList):
    def __init__(self):
        QueryCategoryList.__init__(self)

    @classmethod
    def build_from_config(cls, category_list_config):
        category_list = PiDiskSpaceCategoryList()
        for an_item in category_list_config:
            category = QueryCategory(
                category_id=an_item['id'],
                display_name=an_item['display_name'],
                label=an_item['label'],
                record_parser_class=getattr(record_parser, an_item['record_parser_class']),
                record_parser_arguments=tuple(an_item['record_parser_arguments']),
                value_saver_class=getattr(value_saver, an_item['value_saver_class']),
                value_saver_arguments=tuple(an_item['value_saver_arguments'])
            )
            category_list.append(category)
        return category_list
