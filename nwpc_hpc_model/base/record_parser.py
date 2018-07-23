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
    def __init__(self, index=-1, sep=None):
        RecordParser.__init__(self)
        self.index = index
        self.sep = sep

    def parse(self, record):
        if self.sep is None:
            tokens = record.split()
        else:
            tokens = record.split(self.sep)
        return tokens[self.index]


class RegexGroupParser(RecordParser):
    def __init__(self, group_index):
        RecordParser.__init__(self)
        self.group_index = group_index

    def parse(self, record):
        return record.group(self.group_index)
