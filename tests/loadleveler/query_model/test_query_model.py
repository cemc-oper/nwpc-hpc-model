# coding=utf-8

import unittest
from unittest import mock
import os
import importlib

from nwpc_hpc_model.loadleveler import query_model, query_property, query_category, record_parser, value_saver


class TestQueryModel(unittest.TestCase):
    def setUp(self):
        pass

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
            query_category.QueryCategory("llq.queue_full_date", "Queue Date", "Queue Date",
                                         record_parser.DetailLabelParser, ("Queue Date",),
                                         value_saver.FullDateSaver, ()),
            query_category.QueryCategory("llq.status", "Status", "Status",
                                         record_parser.DetailLabelParser, ("Status",),
                                         value_saver.JobStatusSaver, ())
        ])

        test_case_list = list()

        nwp_output = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/llq.detail.query.output.nwp.txt"
        )
        with open(nwp_output) as nwp_output_file:
            lines = nwp_output_file.readlines()
            model = query_model.LoadLevelerQueryModel.build_from_category_list(lines, category_list)
            model_dict = model.to_dict()
            self.assertTrue('items' in model_dict)
            self.assertEqual(len(model_dict['items']), 3)


    def check_build_model(self, test_case):
        record = test_case['record']
        category_list = test_case['category_list']
        records = test_case['records']

        model = query_model.LoadLevelerQueryModel.build_from_category_list(record, category_list)

        for record in records:
            index = record['index']
            properties = record['properties']
            item = model.items[index]

            for a_prop in properties:
                category_id = a_prop['category_id']
                text = a_prop['text']
                category_index = category_list.index_from_id(category_id)
                p = item.props[category_index]

                self.assertEqual(p.map['text'], text)

    def test_build_model(self):
        check_method = self.check_build_model

        category_list = query_category.QueryCategoryList()

        category_list.extend([
            query_category.QueryCategory("llq.id", "Id", "Job Step Id",
                                         record_parser.DetailLabelParser, ("Job Step Id",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.owner", "Owner", "Owner",
                                         record_parser.DetailLabelParser, ("Owner",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.queue_full_date", "Queue Date", "Queue Date",
                                         record_parser.DetailLabelParser, ("Queue Date",),
                                         value_saver.FullDateSaver, ()),
            query_category.QueryCategory("llq.status", "Status", "Status",
                                         record_parser.DetailLabelParser, ("Status",),
                                         value_saver.JobStatusSaver, ())
        ])

        test_case_list = list()

        nwp_output = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/llq.detail.query.output.nwp.txt"
        )
        with open(nwp_output) as nwp_output_file:
            record = nwp_output_file.readlines()
            test_case_list.append({
                'record': record,
                'category_list': category_list,
                'records': [
                    {
                        'index': 0,
                        'properties': [
                            {
                                'category_id': 'llq.id',
                                'text': 'cma20n04.3473800.0'
                            },
                            {
                                'category_id': 'llq.status',
                                'text': 'R'
                            }
                        ]
                    },
                    {
                        'index': 1,
                        'properties': [
                            {
                                'category_id': 'llq.id',
                                'text': 'cma19n04.3473768.0'
                            },
                            {
                                'category_id': 'llq.status',
                                'text': 'R'
                            }
                        ]
                    }
                ]
            })

        for a_test_case in test_case_list:
            check_method(a_test_case)
