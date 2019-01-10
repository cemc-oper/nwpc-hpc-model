import unittest
import importlib
import datetime

from nwpc_hpc_model.base import value_saver
from nwpc_hpc_model.base.query_property import QueryProperty


class TestValueSaver(unittest.TestCase):
    def setUp(self):
        importlib.reload(value_saver)

    def tearDown(self):
        pass

    def check_string(self, test_case):
        name = test_case['name']
        value = test_case['value']
        text = test_case['text']
        data = test_case['data']

        saver = value_saver.StringSaver()
        item = QueryProperty()

        saver.set_item_value(item, value)

        self.assertEqual(item.map['text'], text)
        self.assertEqual(item.map['data'], data)
        # print("Test passed:", name)

    def test_string(self):
        test_method = self.check_string
        test_case_list = [
            {
                'name': 'id',
                'value': 'cma20n02.2871950.0',
                'text': 'cma20n02.2871950.0',
                'data': 'cma20n02.2871950.0'
            },
            {
                'name': 'owner',
                'value': 'nwp_vfy',
                'text': 'nwp_vfy',
                'data': 'nwp_vfy'
            },
            {
                'name': 'class',
                'value': 'serial',
                'text': 'serial',
                'data': 'serial'
            },
        ]

        for a_test_case in test_case_list:
            test_method(a_test_case)

    def check_number(self, test_case):
        name = test_case['name']
        value = test_case['value']
        text = test_case['text']
        data = test_case['data']

        saver = value_saver.NumberSaver()
        item = QueryProperty()

        saver.set_item_value(item, value)

        self.assertEqual(item.map['text'], text)
        self.assertEqual(item.map['data'], data)
        # print("Test passed:", name)

    def test_number(self):
        test_method = self.check_number
        test_case_list = [
            {
                'name': 'PRI',
                'value': '100',
                'text': '100',
                'data': 100
            }
        ]

        for a_test_case in test_case_list:
            test_method(a_test_case)

    def check_timestamp(self, test_case):
        name = test_case['name']
        value = test_case['value']
        text = test_case['text']
        data = test_case['data']

        saver = value_saver.TimestampSaver()
        item = QueryProperty()

        saver.set_item_value(item, value)

        assert item.map['text'] == text
        assert item.map['data'] == data

    def test_timestamp(self):
        test_method = self.check_timestamp
        test_case_list = [
            {
                'name': 'UTC',
                'value': '1547906480',
                'text': '2019-01-19 14:01:20',
                'data': datetime.datetime(2019, 1, 19, 14, 1, 20)
            }
        ]
        for a_test_case in test_case_list:
            test_method(a_test_case)
