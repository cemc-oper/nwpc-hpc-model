# coding=utf-8
from .query_property import QueryProperty


class QueryItem(object):
    def __init__(self):
        self.props = list()

    def to_dict(self):
        result = dict()
        result['props'] = list()
        for prop in self.props:
            result['props'].append(prop.to_dict())
        return result

    @staticmethod
    def build_from_category_list(record, category_list):
        item = QueryItem()

        for a_category in category_list:
            p = QueryProperty.build_from_category(record, a_category)
            item.props.append(p)

        return item
