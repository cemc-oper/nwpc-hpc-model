# coding=utf-8
import unittest
import os

from nwpc_hpc_model.workload.loadleveler import query_model, query_category, value_saver
from nwpc_hpc_model.workload.loadleveler import record_parser


class TestLlclassDetailQueryModel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

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
            query_category.QueryCategory("llclass.name", "Name", "Name",
                                         record_parser.DetailLabelParser, ("Name",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llclass.free_slots", "Free Slots", "Free_slots",
                                         record_parser.DetailLabelParser, ("Free_slots",),
                                         value_saver.NumberSaver, ()),
            query_category.QueryCategory("llclass.maximum_slots", "Maximum Slots", "Maximum_slots",
                                         record_parser.DetailLabelParser, ("Maximum_slots",),
                                         value_saver.NumberSaver, ())
        ])

        test_case_list = list()

        nwp_output = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llclass/operation.txt"
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
                                'category_id': 'llclass.name',
                                'text': 'operation'
                            },
                            {
                                'category_id': 'llclass.free_slots',
                                'text': '384'
                            },
                            {
                                'category_id': 'llclass.maximum_slots',
                                'text': '2560'
                            }
                        ]
                    }
                ]
            })

        for a_test_case in test_case_list:
            check_method(a_test_case)
