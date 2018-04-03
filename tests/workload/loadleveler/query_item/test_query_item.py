# coding=utf-8
import unittest
import os
import datetime

from nwpc_hpc_model.workload.loadleveler import query_item, query_category, value_saver
from nwpc_hpc_model.workload.loadleveler import record_parser


class TestQueryItem(unittest.TestCase):
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
        category_list = query_category.QueryCategoryList()

        category_list.extend([
            query_category.QueryCategory("llq.id", "Id", "Job Step Id",
                                         record_parser.DetailLabelParser, ("Job Step Id",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.owner", "Owner", "Owner",
                                         record_parser.DetailLabelParser, ("Owner",),
                                         value_saver.StringSaver, ()),
        ])

        serial_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/serial_job_running.txt"
        )
        with open(serial_job_running_file_path) as serial_job_running_file:
            record = serial_job_running_file.readlines()
            item = query_item.QueryItem.build_from_category_list(record, category_list)
            item_dict = item.to_dict()
            self.assertTrue('props' in item_dict)
            self.assertIsInstance(item_dict['props'], list)
            self.assertEqual(len(item_dict['props']), 2)

    def check_build_from_category(self, test_case):
        record = test_case['record']
        category_list = test_case['category_list']
        properties = test_case['properties']

        item = query_item.QueryItem.build_from_category_list(record, category_list)

        for a_property in properties:
            category_id = a_property['category_id']
            value = a_property['value']
            text = a_property['text']
            data = a_property['data']

            index = category_list.index_from_id(category_id)
            if index == -1:
                self.fail("can't find category with id: "+category_id)
            p = item.props[index]
            self.assertEqual(p.map['value'], value)
            self.assertEqual(p.map['text'], text)
            self.assertEqual(p.map['data'], data)

    def test_build_from_category_list(self):
        check_method = self.check_build_from_category

        test_case_list = list()

        serial_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/serial_job_running.txt"
        )
        with open(serial_job_running_file_path) as serial_job_running_file:
            lines = serial_job_running_file.readlines()

            test_case_list.append({
                'record': lines,
                'category_list': self.category_list,
                'properties': [
                    {
                        'category_id': 'llq.id',
                        'value': 'cma20n04.2882680.0',
                        'text': 'cma20n04.2882680.0',
                        'data': 'cma20n04.2882680.0'
                    },
                    {
                        'category_id': "llq.queue_full_date",
                        'value': 'Thu Sep  8 00:09:02 2016',
                        'text': '09/08 00:09',
                        'data': datetime.datetime.strptime("2016/09/08 00:09:02", "%Y/%m/%d %H:%M:%S")
                    },
                    {
                        'category_id': "llq.status",
                        'value': 'Running',
                        'text': 'R',
                        'data': 'R'
                    },
                ]

            })

        for a_test_case in test_case_list:
            check_method(a_test_case)

    def check_property_data(self, test_case):
        record = test_case["record"]
        property_id = test_case["property_id"]
        data = test_case["data"]

        item = query_item.QueryItem.build_from_category_list(record, self.category_list)
        self.assertEqual(query_item.get_property_data(item, property_id), data)

    def test_get_property_data(self):
        check_method = self.check_property_data

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
                    'property_id': "llq.id",
                    'data': 'cma20n04.2882680.0'
                },
                {
                    'record': lines,
                    'property_id': "llq.queue_full_date",
                    'data': datetime.datetime.strptime("2016/09/08 00:09:02", "%Y/%m/%d %H:%M:%S")
                },
                {
                    'record': lines,
                    'property_id': "llq.status",
                    'data': 'R'
                },
            ])

        for a_test_case in test_case_list:
            check_method(a_test_case)
