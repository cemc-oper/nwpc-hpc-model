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

    @classmethod
    def build_from_category_list(cls, record, category_list):
        item = QueryItem()

        for a_category in category_list:
            p = QueryProperty.build_from_category(record, a_category)
            item.props.append(p)

        return item


def get_property_data(job_item: dict or QueryItem, property_id):
    """
    get property data from a job item
    :param job_item: QueryItem or a QueryItem dict.
    :param property_id: property_id
    :return: property data
    """
    result = None
    if isinstance(job_item, dict):
        props = job_item['props']
        for a_prop in props:
            if a_prop['id'] == property_id:
                result = a_prop['data']
                return result
    else:
        props = job_item.props
        for a_prop in props:
            if a_prop.category.id == property_id:
                result = a_prop.map['data']
                return result
    return result
