# coding=utf-8
import datetime
from nwpc_hpc_model.workload.value_saver import ValueSaver, StringSaver, NumberSaver


class FullDateSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        data = datetime.datetime.strptime(value, "%c")

        item.map['text'] = data.strftime("%m/%d %H:%M")
        item.map['value'] = value
        item.map['data'] = data


job_state_list = [
    {"name": "Canceled",           "abbreviation": "CA"},
    {"name": "Checkpointing",      "abbreviation": "CK"},
    {"name": "Completed",          "abbreviation": "C"},
    {"name": "Complete Pending",   "abbreviation": "CP"},
    {"name": "Deferred",           "abbreviation": "D"},
    {"name": "Idle",               "abbreviation": "I"},
    {"name": "Not Queued",         "abbreviation": "NQ"},
    {"name": "Not Run",            "abbreviation": "NR"},
    {"name": "Pending",            "abbreviation": "P"},
    {"name": "Preempted",          "abbreviation": "E"},
    {"name": "Preempt Pending",    "abbreviation": "EP"},
    {"name": "Rejected",           "abbreviation": "X"},
    {"name": "Reject Pending",     "abbreviation": "XP"},
    {"name": "Removed",            "abbreviation": "RM"},
    {"name": "Remove Pending",     "abbreviation": "RP"},
    {"name": "Resume Pending",     "abbreviation": "MP"},
    {"name": "Running",            "abbreviation": "R"},
    {"name": "Starting",           "abbreviation": "ST"},
    {"name": "System Hold",        "abbreviation": "S"},
    {"name": "Terminated",         "abbreviation": "TX"},
    {"name": "User & System Hold", "abbreviation": "HS"},
    {"name": "User Hold",          "abbreviation": "H"},
    {"name": "Vacated",            "abbreviation": "V"},
    {"name": "Vacate Pending",     "abbreviation": "VP"}
]


class JobStatusSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        value_length = len(value)
        if value_length == 1 or value_length == 2:
            item.map['text'] = value
            item.map['value'] = value
            item.map['data'] = value
            return

        for a_job_state in job_state_list:
            if a_job_state['name'] == value:
                item.map['text'] = a_job_state['abbreviation']
                item.map['value'] = value
                item.map['data'] = a_job_state['abbreviation']
                return

        item.map['text'] = value
        item.map['value'] = value
        item.map['data'] = value
        return
