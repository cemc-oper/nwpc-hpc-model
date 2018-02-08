# coding: utf-8
from pathlib import Path

from nwpc_hpc_model.workload.slurm import SlurmQueryModel, SlurmQueryCategoryList
from nwpc_hpc_model.workload import QueryCategory, record_parser, value_saver


class TestSinfoQueryInfo(object):

    def test_to_dict(self):
        category_list = SlurmQueryCategoryList()

        category_list.extend([
            QueryCategory("sinfo.partition", "Partition", "PARTITION",
                          record_parser.TokenRecordParser,  (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.avail", "Avail", "AVAIL",
                          record_parser.TokenRecordParser,  (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.time_limit", "Time Limit", "TIMELIMIT",
                          record_parser.TokenRecordParser,  (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.nodes", "Nodes", "NODES",
                          record_parser.TokenRecordParser,  (-1,),
                          value_saver.NumberSaver, ()),
            QueryCategory("sinfo.state", "State", "STATE",
                          record_parser.TokenRecordParser,  (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.node_list", "Node List", "NODELIST",
                          record_parser.TokenRecordParser,  (-1,),
                          value_saver.StringSaver, ()),
        ])

        test_case_list = list()

        nwp_output = Path(
            Path(__file__).parent,
            "../data/sinfo/default.txt"
        )
        with open(nwp_output) as nwp_output_file:
            lines = nwp_output_file.read().split('\n')
            model = SlurmQueryModel.build_from_table_category_list(lines, category_list)
            model_dict = model.to_dict()
            assert(('items' in model_dict) is True)
            assert(len(model_dict['items']) == 12)

    def check_build_model(self, test_case):
        record = test_case['record']
        category_list = test_case['category_list']
        records = test_case['records']

        model = SlurmQueryModel.build_from_table_category_list(record, category_list)

        for record in records:
            index = record['index']
            properties = record['properties']
            item = model.items[index]

            for a_prop in properties:
                category_id = a_prop['category_id']
                text = a_prop['text']
                category_index = category_list.index_from_id(category_id)
                p = item.props[category_index]

                assert(p.map['text'] == text)

    def test_build_model(self):
        check_method = self.check_build_model

        category_list = SlurmQueryCategoryList()

        category_list.extend([
            QueryCategory("sinfo.partition", "Partition", "PARTITION",
                          record_parser.TokenRecordParser, (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.avail", "Avail", "AVAIL",
                          record_parser.TokenRecordParser, (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.time_limit", "Time Limit", "TIMELIMIT",
                          record_parser.TokenRecordParser, (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.nodes", "Nodes", "NODES",
                          record_parser.TokenRecordParser, (-1,),
                          value_saver.NumberSaver, ()),
            QueryCategory("sinfo.state", "State", "STATE",
                          record_parser.TokenRecordParser, (-1,),
                          value_saver.StringSaver, ()),
            QueryCategory("sinfo.node_list", "Node List", "NODELIST",
                          record_parser.TokenRecordParser, (-1,),
                          value_saver.StringSaver, ()),
        ])

        test_case_list = list()

        nwp_output = Path(
            Path(__file__).parent,
            "../data/sinfo/default.txt"
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
                                'category_id': 'sinfo.partition',
                                'text': 'serial'
                            },
                            {
                                'category_id': 'sinfo.state',
                                'text': 'idle'
                            }
                        ]
                    },
                    {
                        'index': 1,
                        'properties': [
                            {
                                'category_id': 'sinfo.partition',
                                'text': 'normal'
                            },
                            {
                                'category_id': 'sinfo.state',
                                'text': 'drain'
                            }
                        ]
                    }
                ]
            })

        for a_test_case in test_case_list:
            check_method(a_test_case)
