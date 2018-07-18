# coding=utf-8
from nwpc_hpc_model.base.record_parser import *


class RegexGroupParser(RecordParser):
    def __init__(self, group_index):
        RecordParser.__init__(self)
        self.group_index = group_index

    def parse(self, record):
        return record.group(self.group_index)
