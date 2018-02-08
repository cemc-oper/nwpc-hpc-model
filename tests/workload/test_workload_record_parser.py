# coding=utf-8

from nwpc_hpc_model.workload import record_parser


class TestRecordParser(object):
    def test_token_record_parser(self):
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
            index = case["record_parser"]["args"]["index"]

            parser = record_parser.TokenRecordParser(index)
            parser_value = parser.parse(case_line)
            assert(parser_value == value)

        for test_case in test_cases:
            check_parser(test_case)
