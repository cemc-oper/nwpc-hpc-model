# coding=utf-8
import copy


class QueryProperty(object):
    def __init__(self):
        self.map = dict()
        self.category = None

    def to_dict(self):
        result = copy.deepcopy(self.map)
        if self.category is not None:
            result['id'] = self.category.id
        return result

    @staticmethod
    def build_from_category(record, category):
        prop = QueryProperty()

        prop.category = category
        value = category.record_parser.parse(record)
        category.value_saver.set_item_value(prop, value)
        return prop
