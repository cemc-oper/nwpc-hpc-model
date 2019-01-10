import unittest
import importlib
import datetime

from nwpc_hpc_model.workload.loadleveler import value_saver
from nwpc_hpc_model.workload.loadleveler import QueryProperty


class TestValueSaver(unittest.TestCase):
    def setUp(self):
        importlib.reload(value_saver)

    def tearDown(self):
        pass

    def check_full_date(self, test_case):
        name = test_case['name']
        value = test_case['value']
        text = test_case['text']
        data = test_case['data']

        saver = value_saver.FullDateSaver()
        item = QueryProperty()

        saver.set_item_value(item, value)

        self.assertEqual(item.map['text'], text)
        self.assertEqual(item.map['data'], data)
        # print("Test passed:", name)

    def test_full_date(self):
        test_method = self.check_full_date
        test_case_list = [
            {
                'name': '0',
                'value': 'Wed Sep  7 07:00:02 2016',
                'text': '09/07 07:00',
                'data': datetime.datetime.strptime("2016/09/07 07:00:02", "%Y/%m/%d %H:%M:%S")
            },
            {
                'name': '1',
                'value': 'Tue Aug 23 01:54:30 2016',
                'text': '08/23 01:54',
                'data': datetime.datetime.strptime("2016/08/23 01:54:30", "%Y/%m/%d %H:%M:%S")
            }
        ]

        for a_test_case in test_case_list:
            test_method(a_test_case)

    def check_job_state(self, test_case):
        name = test_case['name']
        value = test_case['value']
        text = test_case['text']
        data = test_case['data']

        saver = value_saver.JobStatusSaver()
        item = QueryProperty()

        saver.set_item_value(item, value)

        self.assertEqual(item.map['value'], value)
        self.assertEqual(item.map['text'], text)
        self.assertEqual(item.map['data'], data)
        # print("Test passed:", name)

    def test_job_state(self):
        test_method = self.check_job_state
        test_case_list = [
            {
                'name': 'R',
                'value': 'R',
                'text': 'R',
                'data': 'R'
            },
            {
                'name': 'Running',
                'value': 'Running',
                'text': 'R',
                'data': 'R'
            },
            {
                'name': 'RP',
                'value': 'RP',
                'text': 'RP',
                'data': 'RP'
            },
            {
                'name': 'Remove Pending',
                'value': 'Remove Pending',
                'text': 'RP',
                'data': 'RP'
            },

        ]

        for a_test_case in test_case_list:
            test_method(a_test_case)
