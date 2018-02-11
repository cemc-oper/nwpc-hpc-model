# coding: utf-8
from pathlib import Path

from nwpc_hpc_model.workload.slurm import SlurmQueryModel, SlurmQueryCategoryList
from nwpc_hpc_model.workload import QueryCategory, record_parser, value_saver


class TestSqueueQueryInfo(object):
    def check_build_model(self, test_case):
        record = test_case['record']
        category_list = test_case['category_list']
        records = test_case['records']

        model = SlurmQueryModel.build_from_table_category_list(record, category_list, sep='|')

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
            QueryCategory("squeue.account", "Account", "ACCOUNT",
                          record_parser.TokenRecordParser, (-1, '|'),
                          value_saver.StringSaver, ()),
            QueryCategory("squeue.job_id", "Job ID", "JOBID",
                          record_parser.TokenRecordParser, (-1, '|'),
                          value_saver.StringSaver, ()),
            QueryCategory("squeue.command", "Command", "COMMAND",
                          record_parser.TokenRecordParser, (-1, '|'),
                          value_saver.StringSaver, ()),
            QueryCategory("squeue.nodes", "Nodes", "NODES",
                          record_parser.TokenRecordParser, (-1, '|'),
                          value_saver.NumberSaver, ()),
            QueryCategory("squeue.state", "State", "STATE",
                          record_parser.TokenRecordParser, (-1, '|'),
                          value_saver.StringSaver, ()),
            QueryCategory("squeue.work_dir", "Work dir", "WORK_DIR",
                          record_parser.TokenRecordParser, (-1, '|'),
                          value_saver.StringSaver, ()),
        ])

        test_case_list = list()

        nwp_output = Path(
            Path(__file__).parent,
            "../data/squeue/queue_all.txt"
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
                                'category_id': 'squeue.job_id',
                                'text': '129417'
                            },
                            {
                                'category_id': 'squeue.state',
                                'text': 'RUNNING'
                            }
                        ]
                    },
                    {
                        'index': 1,
                        'properties': [
                            {
                                'category_id': 'squeue.command',
                                'text': '/g1/u/nwp_xp/tmp/s.job'
                            },
                            {
                                'category_id': 'squeue.state',
                                'text': 'RUNNING'
                            }
                        ]
                    }
                ]
            })

        for a_test_case in test_case_list:
            check_method(a_test_case)
