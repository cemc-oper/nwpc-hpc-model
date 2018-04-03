# coding=utf-8
import unittest
import os
import datetime

from nwpc_hpc_model.workload.loadleveler import query_property, query_category, value_saver
from nwpc_hpc_model.workload.loadleveler import record_parser


class TestQueryProperty(unittest.TestCase):
    def setUp(self):
        self.category_list = query_category.QueryCategoryList()

        self.category_list.extend([
            query_category.QueryCategory("llq.id", "Id", "Job Step Id",
                                         record_parser.DetailLabelParser, ("Job Step Id",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.owner", "Owner", "Owner",
                                         record_parser.DetailLabelParser, ("Owner",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.queue_full_date", "Queue Date", "Queue Date",
                                         record_parser.DetailLabelParser, ("Queue Date",),
                                         value_saver.FullDateSaver, ()),
            query_category.QueryCategory("llq.job_script", "Job Script", "Cmd",
                                         record_parser.DetailLabelParser, ("Cmd",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.status", "Status", "Status",
                                         record_parser.DetailLabelParser, ("Status",),
                                         value_saver.JobStatusSaver, ())
        ])

    def tearDown(self):
        pass

    def test_to_dict(self):
        # TODO: test_to_dict
        pass

    def check_query_item(self, test_case):
        record = test_case["record"]
        category = test_case["category"]
        value = test_case["value"]
        text = test_case["text"]
        data = test_case["data"]

        item = query_property.QueryProperty.build_from_category(
            record=record,
            category=category
        )
        self.assertIsInstance(item, query_property.QueryProperty)
        self.assertEqual(item.map['value'], value)
        self.assertEqual(item.map['text'], text)
        self.assertEqual(item.map['data'], data)
        self.assertEqual(item.category, category)

    def test_create_query_property(self):
        check_method = self.check_query_item

        test_case_list = list()

        serial_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/serial_job_running.txt"
        )

        with open(serial_job_running_file_path) as serial_job_running_file:
            lines = serial_job_running_file.readlines()

            test_case_list.extend([
                {
                    'record': lines,
                    'category': self.category_list.category_from_id("llq.id"),

                    'value': 'cma20n04.2882680.0',
                    'text': 'cma20n04.2882680.0',
                    'data': 'cma20n04.2882680.0'
                },
                {
                    'record': lines,
                    'category': self.category_list.category_from_id("llq.queue_full_date"),

                    'value': 'Thu Sep  8 00:09:02 2016',
                    'text': '09/08 00:09',
                    'data': datetime.datetime.strptime("2016/09/08 00:09:02", "%Y/%m/%d %H:%M:%S")
                },
                {
                    'record': lines,
                    'category': self.category_list.category_from_id("llq.status"),

                    'value': 'Running',
                    'text': 'R',
                    'data': 'R'
                },
            ])

        for a_test_case in test_case_list:
            check_method(a_test_case)