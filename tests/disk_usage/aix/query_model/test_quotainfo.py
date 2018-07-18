# coding: utf-8
from pathlib import Path
import yaml

from nwpc_hpc_model.disk_usage.aix import AixDiskUsageQueryModel, QueryCategory, \
    AixDiskUsageCategoryList, record_parser, value_saver


class TestQuotaInfo(object):
    def check_build_model(self, test_case):
        record = test_case['record']
        category_list = test_case['category_list']
        records = test_case['records']

        model = AixDiskUsageQueryModel.build_from_category_list(record, category_list)

        for record in records:
            index = record['index']
            properties = record['properties']
            item = model.items[index]

            for a_prop in properties:
                category_id = a_prop['category_id']
                data = a_prop['data']
                category_index = category_list.index_from_id(category_id)
                p = item.props[category_index]

                assert(p.map['data'] == data)

    # def test_build_model(self):
    #     check_method = self.check_build_model
    #
    #     category_list = PiDiskUsageCategoryList()
    #
    #     category_list.extend([
    #         QueryCategory("disk_usage.dir", "Direcotry", "dir",
    #                       record_parser.TokenRecordParser, (0,),
    #                       value_saver.StringSaver, ()),
    #         QueryCategory("disk_usage.total_size", "Size", "Size(GB)",
    #                       record_parser.TokenRecordParser, (1,),
    #                       value_saver.NumberSaver, ()),
    #         QueryCategory("disk_usage.used_size", "Used", "Used(GB)",
    #                       record_parser.TokenRecordParser, (2,),
    #                       value_saver.NumberSaver, ()),
    #         QueryCategory("disk_usage.avail_size", "Avail", "Avail(GB)",
    #                       record_parser.TokenRecordParser, (3,),
    #                       value_saver.NumberSaver, ()),
    #         QueryCategory("disk_usage.used_percent", "Used Percent", "Use%",
    #                       record_parser.TokenRecordParser, (4,),
    #                       value_saver.NumberSaver, ()),
    #         QueryCategory("disk_usage.type", "Type", "Type",
    #                       record_parser.TokenRecordParser, (4,),
    #                       value_saver.StringSaver, ()),
    #     ])
    #
    #     test_case_list = list()
    #
    #     nwp_output = Path(
    #         Path(__file__).parent,
    #         "../../data/pi/quotainfo_nwp.txt"
    #     )
    #
    #     with open(nwp_output) as nwp_output_file:
    #         record = nwp_output_file.readlines()
    #         test_case_list.append({
    #             'record': record,
    #             'category_list': category_list,
    #             'records': [
    #                 {
    #                     'index': 0,
    #                     'properties': [
    #                         {
    #                             'category_id': 'disk_usage.dir',
    #                             'data': '/g1'
    #                         },
    #                         {
    #                             'category_id': 'disk_usage.total_size',
    #                             'data': 20.0
    #                         },
    #                         {
    #                             'category_id': 'disk_usage.used_size',
    #                             'data': 1.23
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     'index': 1,
    #                     'properties': [
    #                         {
    #                             'category_id': 'disk_usage.dir',
    #                             'data': '/g2'
    #                         },
    #                         {
    #                             'category_id': 'disk_usage.total_size',
    #                             'data': 900000.0
    #                         },
    #                         {
    #                             'category_id': 'disk_usage.used_size',
    #                             'data': 49788.64
    #                         }
    #                     ]
    #                 }
    #             ]
    #         })
    #
    #     for a_test_case in test_case_list:
    #         check_method(a_test_case)

    def test_build_model_using_config_file(self):
        check_method = self.check_build_model

        config_file_path = Path(
            Path(__file__).parent,
            "../../../../nwpc_hpc_model/disk_usage/aix/conf/disk_usage.config.yml"
        )

        with open(config_file_path) as f:
            category_list_config = yaml.load(f)

        category_list = AixDiskUsageCategoryList.build_from_config(category_list_config['category_list'])

        test_case_list = list()

        nwp_output = Path(
            Path(__file__).parent,
            "../../data/aix/cmquota_nwp.txt"
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
                                'category_id': 'disk_usage.file_system',
                                'data': 'cma_g1'
                            },
                            {
                                'category_id': 'disk_usage.block_limits.current',
                                'data': 28616415232
                            },
                            {
                                'category_id': 'disk_usage.block_limits.quota',
                                'data': 32212254720
                            },
                            {
                                'category_id': 'disk_usage.file_limits.quota',
                                'data': 0
                            }
                        ]
                    },
                    {
                        'index': 1,
                        'properties': [
                            {
                                'category_id': 'disk_usage.file_system',
                                'data': 'cma_u'
                            },
                            {
                                'category_id': 'disk_usage.block_limits.current',
                                'data': 111307008
                            },
                            {
                                'category_id': 'disk_usage.block_limits.quota',
                                'data': 209715200
                            }
                        ]
                    }
                ]
            })

        for a_test_case in test_case_list:
            check_method(a_test_case)

