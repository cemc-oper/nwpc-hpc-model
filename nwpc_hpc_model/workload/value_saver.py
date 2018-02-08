# coding=utf-8


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
