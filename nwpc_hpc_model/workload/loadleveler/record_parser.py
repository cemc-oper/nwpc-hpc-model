# coding=utf-8
import pathlib
from nwpc_hpc_model.base.record_parser import *


class DetailLabelParser(RecordParser):
    def __init__(self, label):
        RecordParser.__init__(self)

        self.label = label

    def __deepcopy__(self, memodict={}):
        return DetailLabelParser(self.label)

    def parse(self, record):
        for line in record:
            index = line.find(': ')
            if index == -1:
                continue
            label = line[0:index].strip()
            if label != self.label:
                continue
            value = line[index+2:].strip()
            return value
        return ""


class LlqFilePathParser(DetailLabelParser):
    def __init__(self, label):
        DetailLabelParser.__init__(self, label)

    @staticmethod
    def find_initial_working_dir(record):
        parser = DetailLabelParser("Initial Working Dir")
        value = parser.parse(record)
        return value

    def parse(self, record):
        parser = DetailLabelParser(self.label)
        value = parser.parse(record)

        if value.startswith('.'):
            initial_working_dir = LlqFilePathParser.find_initial_working_dir(record)
            value = str(pathlib.PurePosixPath(initial_working_dir, value))

        return value


class LlqJobScriptParser(RecordParser):
    def __init__(self):
        RecordParser.__init__(self)

    @staticmethod
    def find_step_type_value(record):
        parser = DetailLabelParser("Step Type")
        value = parser.parse(record)
        return value

    def parse(self, record):
        step_type = LlqJobScriptParser.find_step_type_value(record)

        if step_type == "General Parallel":
            script_label = "Executable"
        elif step_type == "Serial":
            script_label = "Cmd"
        else:
            return ""

        file_path_parser = LlqFilePathParser(script_label)
        value = file_path_parser.parse(record)
        return value
