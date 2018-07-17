# coding: utf-8


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
