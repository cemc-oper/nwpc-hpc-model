# coding=utf-8

from nwpc_hpc_model.base import record_parser


class TestRecordParser(object):
    @classmethod
    def check_parser(cls, parser_class, case):
        record = case["record"]
        value = case["value"]
        name = case["name"]
        record_parser_args = case["record_parser"]["args"]

        parser = parser_class(**record_parser_args)
        parser_value = parser.parse(record)
        assert parser_value == value

    def test_default_token_parser(self):
        line = "operation    up   infinite     26  drain " \
               "cmac[0085-0086,0092,0109-0110,0707-0722,0775,0808,0961,1301,1369]"
        test_cases = [
            {
                "name": "sinfo.default_query.simple.1",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 0
                    }
                },
                "value": "operation"
            },
            {
                "name": "sinfo.default_query.simple.2",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 2
                    }
                },
                "value": "infinite"
            },
            {
                "name": "sinfo.default_query.simple.3",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 4
                    }
                },
                "value": "drain"
            },
            {
                "name": "sinfo.default_query.simple.3",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 5
                    }
                },
                "value": "cmac[0085-0086,0092,0109-0110,0707-0722,0775,0808,0961,1301,1369]"
            }
        ]

        for test_case in test_cases:
            TestRecordParser.check_parser(record_parser.TokenRecordParser, test_case)

    def test_custom_token_parser(self):
        line = "nwp_xp|(null)|1|0|NONE"
        test_cases = [
            {
                "name": "sinfo.default_query.simple.1",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 0,
                        "sep": '|'
                    }
                },
                "value": "nwp_xp"
            },
            {
                "name": "sinfo.default_query.simple.2",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 1,
                        "sep": '|'
                    }
                },
                "value": "(null)"
            },
            {
                "name": "sinfo.default_query.simple.3",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 2,
                        "sep": '|'
                    }
                },
                "value": "1"
            },
            {
                "name": "sinfo.default_query.simple.3",
                "record": line,
                "record_parser": {
                    "args": {
                        "index": 3,
                        "sep": '|'
                    }
                },
                "value": "0"
            }
        ]

        for test_case in test_cases:
            TestRecordParser.check_parser(record_parser.TokenRecordParser, test_case)

    def test_dict_parser(self):
        test_cases = [
            {
                "name": "sinfo.query.simple.1",
                "record": {
                    'comment': 'GRAPES',
                    'run_time_str': '01:06:13'
                },
                "record_parser": {
                    "args": {
                        "key": 'comment'
                    }
                },
                "value": "GRAPES"
            }
        ]

        for test_case in test_cases:
            TestRecordParser.check_parser(record_parser.DictRecordParser, test_case)
