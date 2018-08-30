# coding=utf-8

from nwpc_hpc_model.base import record_parser


class TestRecordParser(object):
    def test_default_token_parser(self):
        line = "operation    up   infinite     26  drain cmac[0085-0086,0092,0109-0110,0707-0722,0775,0808,0961,1301,1369]"
        test_cases = [
            {
                "name": "sinfo.default_query.simple.1",
                "line": line,
                "record_parser": {
                    "args": {
                        "index": 0
                    }
                },
                "value": "operation"
            },
            {
                "name": "sinfo.default_query.simple.2",
                "line": line,
                "record_parser": {
                    "args": {
                        "index": 2
                    }
                },
                "value": "infinite"
            },
            {
                "name": "sinfo.default_query.simple.3",
                "line": line,
                "record_parser": {
                    "args": {
                        "index": 4
                    }
                },
                "value": "drain"
            },
            {
                "name": "sinfo.default_query.simple.3",
                "line": line,
                "record_parser": {
                    "args": {
                        "index": 5
                    }
                },
                "value": "cmac[0085-0086,0092,0109-0110,0707-0722,0775,0808,0961,1301,1369]"
            }
        ]

        def check_parser(case):
            case_line = case["line"]
            value = case["value"]
            name = case["name"]
            record_parser_args = case["record_parser"]["args"]

            parser = record_parser.TokenRecordParser(**record_parser_args)
            parser_value = parser.parse(case_line)
            assert(parser_value == value)

        for test_case in test_cases:
            check_parser(test_case)

    def test_custom_token_parser(self):
        line = "nwp_xp|(null)|1|0|NONE"
        test_cases = [
            {
                "name": "sinfo.default_query.simple.1",
                "line": line,
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
                "line": line,
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
                "line": line,
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
                "line": line,
                "record_parser": {
                    "args": {
                        "index": 3,
                        "sep": '|'
                    }
                },
                "value": "0"
            }
        ]

        def check_parser(case):
            case_line = case["line"]
            value = case["value"]
            name = case["name"]
            record_parser_args = case["record_parser"]["args"]

            parser = record_parser.TokenRecordParser(**record_parser_args)
            parser_value = parser.parse(case_line)
            assert (parser_value == value)

        for test_case in test_cases:
            check_parser(test_case)