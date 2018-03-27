# coding=utf-8
import datetime


class ValueSaver(object):
    def __init__(self):
        pass

    def set_item_value(self, item, value):
        pass


class StringSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        item.map['text'] = value
        item.map['value'] = value
        item.map['data'] = value


class NumberSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        data = float(value)
        item.map['text'] = value
        item.map['value'] = value
        item.map['data'] = data


class DateTimeSaver(ValueSaver):
    def __init__(self, datetime_format):
        ValueSaver.__init__(self)
        self.datetime_format = datetime_format

    def set_item_value(self, item, value):
        data = datetime.datetime.strptime(value, self.datetime_format)

        item.map['text'] = data.strftime("%Y-%m-%d %H:%M:%S")
        item.map['value'] = value
        item.map['data'] = data
