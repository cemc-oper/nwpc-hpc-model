# coding: utf-8
class Filter(object):
    def __init__(self):
        self.conditions = list()
        pass

    def filter(self, job_items):
        target_job_items = list()
        for a_job_item in job_items:
            is_fit = True
            for a_condition in self.conditions:
                if not a_condition.is_fit(a_job_item):
                    is_fit = False
                    break
            if is_fit:
                target_job_items.append(a_job_item)
        return target_job_items
