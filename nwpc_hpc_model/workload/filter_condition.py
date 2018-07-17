# coding: utf-8
from nwpc_hpc_model.base.query_item import get_property_data


class FilterCondition(object):
    def __init__(self):
        pass

    def is_fit(self, job_item):
        return True


class PropertyFilterCondition(FilterCondition):
    def __init__(self, property_id, data_checker, data_parser=get_property_data):
        FilterCondition.__init__(self)
        self.property_id = property_id
        self.data_checker = data_checker
        self.data_parser = data_parser

    def is_fit(self, job_item):
        value = self.data_parser(job_item, self.property_id)
        if self.data_checker(value):
            return True
        else:
            return False


def create_equal_value_checker(expect_value):
    def value_checker(value):
        if value == expect_value:
            return True
        else:
            return False

    return value_checker


def create_greater_value_checker(expect_value):
    def value_checker(value):
        if value > expect_value:
            return True
        else:
            return False

    return value_checker


def create_less_value_checker(expect_value):
    def value_checker(value):
        if value < expect_value:
            return True
        else:
            return False

    return value_checker


def create_in_value_checker(expect_values):
    def value_checker(value):
        if value in expect_values:
            return True
        else:
            return False
    return value_checker


def create_value_in_checker(expect_value):
    def value_checker(value):
        if expect_value in value:
            return True
        else:
            return False
    return value_checker
