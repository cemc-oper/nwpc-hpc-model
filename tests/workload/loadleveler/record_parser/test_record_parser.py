# coding=utf-8
import unittest
import os
import importlib
import copy

from nwpc_hpc_model.workload.loadleveler import record_parser


class TestRecordParser(unittest.TestCase):
    def setUp(self):
        importlib.reload(record_parser)

    def tearDown(self):
        pass

    def test_deep_copy(self):
        parser_one = record_parser.DetailLabelParser("label-1")
        parser_two = copy.deepcopy(parser_one)
        parser_two.label = "label-2"
        self.assertNotEqual(parser_one.label, parser_two.label)

    def check_llq_detail_query_record_parser(self, test_case):
        lines = test_case["lines"]
        label = test_case["label"]
        value = test_case["value"]
        name = test_case["name"]

        parser = record_parser.DetailLabelParser(label)
        parser_value = parser.parse(lines)
        self.assertEqual(parser_value, value)
        # print("Test passed:", name)

    def test_llq_detail_query_record_parser(self):
        serial_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/serial_job_running.txt"
        )
        test_case_list = []
        with open(serial_job_running_file_path) as serial_job_running_file:
            lines = serial_job_running_file.readlines()
            test_case_list.extend([
                {
                    "name": "llq.serial_job.running.job_step_id",
                    "lines": lines,
                    "label": "Job Step Id",
                    "value": "cma20n04.2882680.0"
                },
                {
                    "name": "llq.serial_job.running.cmd",
                    "lines": lines,
                    "label": "Cmd",
                    "value": "/cma/g1/nwp/SMSOUT/gmf_grapes_gfs_v2_0/grapes_global/12/post/postp_240.job1"
                },
                {
                    "name": "llq.serial_job.running.queue_date",
                    "lines": lines,
                    "label": "Queue Date",
                    "value": "Thu Sep  8 00:09:02 2016"
                },
                {
                    "name": "llq.serial_job.running.cpu_per_core",
                    "lines": lines,
                    "label": "Cpus Per Core",
                    "value": "0"
                },
                {
                    "name": "llq.serial_job.running.task_affinity",
                    "lines": lines,
                    "label": "Task Affinity",
                    "value": ""
                },
            ])

        for a_test_case in test_case_list:
            self.check_llq_detail_query_record_parser(a_test_case)

    def check_llq_script_record_parser(self, test_case):
        lines = test_case["lines"]
        value = test_case["value"]
        name = test_case["name"]

        parser = record_parser.LlqJobScriptParser()
        parser_value = parser.parse(lines)
        self.assertEqual(parser_value, value)
        # print("Test passed:", name)

    def test_llq_script_record_parser(self):
        check_method = self.check_llq_script_record_parser
        serial_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/serial_job_running.txt"
        )
        test_case_list = []
        with open(serial_job_running_file_path) as serial_job_running_file:
            lines = serial_job_running_file.readlines()
            test_case_list.extend([
                {
                    "name": "llq.serial_job.running.job_script",
                    "lines": lines,
                    "value": "/cma/g1/nwp/SMSOUT/gmf_grapes_gfs_v2_0/grapes_global/12/post/postp_240.job1"
                }
            ])

        parallel_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/parallel_job_running.txt"
        )
        with open(parallel_job_running_file_path) as parallel_job_running_file:
            lines = parallel_job_running_file.readlines()
            test_case_list.extend([
                {
                    "name": "llq.parallel_job.running.job_script",
                    "lines": lines,
                    "value": "/cma/g1/nwp_qu/SMSOUT/rafs/cold/00/model/fcst.job1"
                }
            ])

        for a_test_case in test_case_list:
            check_method(a_test_case)

    def check_llq_file_path_record_parser(self, test_case):
        lines = test_case["lines"]
        value = test_case["value"]
        name = test_case["name"]
        label = test_case["label"]

        parser = record_parser.LlqFilePathParser(label)
        parser_value = parser.parse(lines)
        self.assertEqual(parser_value, value)
        # print("Test passed:", name)

    def test_llq_file_path_record_parser(self):
        check_method = self.check_llq_file_path_record_parser
        serial_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/serial_job_running.txt"
        )
        test_case_list = []
        with open(serial_job_running_file_path) as serial_job_running_file:
            lines = serial_job_running_file.readlines()
            test_case_list.extend([
                {
                    "name": "llq.serial_job.running.out",
                    "lines": lines,
                    "value": "/cma/g1/nwp/SMSOUT/gmf_grapes_gfs_v2_0/grapes_global/12/post/postp_240.1",
                    "label": "Out",
                },
                {
                    "name": "llq.serial_job.running.err",
                    "lines": lines,
                    "value": "/cma/g1/nwp/SMSOUT/gmf_grapes_gfs_v2_0/grapes_global/12/post/postp_240.1.err",
                    "label": "Err",
                }
            ])

        parallel_job_running_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/detail_query/llq/parallel_job_running_3.txt"
        )
        with open(parallel_job_running_file_path) as parallel_job_running_file:
            lines = parallel_job_running_file.readlines()
            test_case_list.extend([
                {
                    "name": "llq.parallel_job.running.out",
                    "lines": lines,
                    "value": "/cmb/g3/chenjing/WRF-REPS/operation/gefs_ruc/2017052112/p02/tmpdir_wrf/"
                             "printout/wrf_6173907.out",
                    "label": "Out",
                },
                {
                    "name": "llq.parallel_job.running.err",
                    "lines": lines,
                    "value": "/cmb/g3/chenjing/WRF-REPS/operation/gefs_ruc/2017052112/p02/tmpdir_wrf/"
                             "printout/wrf_6173907.err",
                    "label": "Err",
                }
            ])

        for a_test_case in test_case_list:
            check_method(a_test_case)

    def check_table_record_parser(self, test_case):
        line = test_case["line"]
        value = test_case["value"]
        name = test_case["name"]
        begin_pos = test_case["record_parser"]["args"]["begin_pos"]
        end_pos = test_case["record_parser"]["args"]["end_pos"]

        parser = record_parser.TableRecordParser(begin_pos, end_pos)
        parser_value = parser.parse(line)
        self.assertEqual(parser_value, value)
        # print("Test passed:", name)

    def test_table_record_parser(self):
        check_method = self.check_table_record_parser
        simple_default_query_file_path = os.path.join(
            os.path.dirname(__file__),
            "../data/default_query/llq/simple.default.query.txt"
        )

        test_case_list = []
        with open(simple_default_query_file_path) as simple_default_query_file:
            lines = simple_default_query_file.readlines()
            test_case_list.extend([
                {
                    "name": "llq.default_query.simple.1",
                    "line": lines[2].strip(),
                    "record_parser": {
                        "args": {
                            "begin_pos": 0,
                            "end_pos": 24
                        }
                    },
                    "value": "cma19n04.4192420.0"
                },
                {
                    "name": "llq.default_query.simple.1",
                    "line": lines[2].strip(),
                    "record_parser": {
                        "args": {
                            "begin_pos": 25,
                            "end_pos": 35
                        }
                    },
                    "value": "nwp"
                },
                {
                    "name": "llq.default_query.simple.1",
                    "line": lines[2].strip(),
                    "record_parser": {
                        "args": {
                            "begin_pos": 36,
                            "end_pos": 47
                        }
                    },
                    "value": "1/13 03:38"
                },
                {
                    "name": "llq.default_query.simple.1",
                    "line": lines[2].strip(),
                    "record_parser": {
                        "args": {
                            "begin_pos": 48,
                            "end_pos": 50
                        }
                    },
                    "value": "R"
                },
                {
                    "name": "llq.default_query.simple.1",
                    "line": lines[2].strip(),
                    "record_parser": {
                        "args": {
                            "begin_pos": 51,
                            "end_pos": 54
                        }
                    },
                    "value": "100"
                },
                {
                    "name": "llq.default_query.simple.1",
                    "line": lines[2].strip(),
                    "record_parser": {
                        "args": {
                            "begin_pos": 55,
                            "end_pos": 67
                        }
                    },
                    "value": "operation"
                },
                {
                    "name": "llq.default_query.simple.1",
                    "line": lines[2].strip(),
                    "record_parser": {
                        "args": {
                            "begin_pos": 68,
                            "end_pos": 79
                        }
                    },
                    "value": "cma02n05"
                }
            ])
        for a_test_case in test_case_list:
            check_method(a_test_case)
