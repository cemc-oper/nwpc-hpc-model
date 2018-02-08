# coding=utf-8


class RecordParser(object):
    def __init__(self):
        pass

    def parse(self, record):
        pass


class TableRecordParser(RecordParser):
    def __init__(self, begin_pos, end_pos):
        RecordParser.__init__(self)
        self.begin_pos = int(begin_pos)
        self.end_pos = int(end_pos)

    def parse(self, record):
        return record[self.begin_pos:self.end_pos].strip()


class TokenRecordParser(RecordParser):
    def __init__(self, index):
        RecordParser.__init__(self)
        self.index = index

    def parse(self, record):
        tokens = record.split()
        return tokens[self.index]
