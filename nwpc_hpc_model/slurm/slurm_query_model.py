# coding: utf-8
from nwpc_hpc_model.workload_scheme import QueryModel


class SlurmQueryModel(QueryModel):
    def __init__(self):
        QueryModel.__init__(self)

    @classmethod
    def build_from_category_list(cls, record, category_list):
        pass
