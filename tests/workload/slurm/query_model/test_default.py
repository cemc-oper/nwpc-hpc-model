# coding: utf-8
from pathlib import Path

from nwpc_hpc_model.workload.slurm import SlurmQueryModel, SlurmQueryCategoryList
from nwpc_hpc_model.workload.slurm import QueryCategory, record_parser, value_saver


def test_empty_build_from_table_category_list():
    category_list = SlurmQueryCategoryList()
    category_list.extend([
        QueryCategory("sinfo.partition", "Partition", "PARTITION",
                      record_parser.TokenRecordParser,  (-1,),
                      value_saver.StringSaver, ())])

    model = SlurmQueryModel.build_from_table_category_list([], category_list)
    assert model is None

    model = SlurmQueryModel.build_from_table_category_list(
        ['PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST',
         ''], category_list
    )
    assert len(model.items) == 0

    model = SlurmQueryModel.build_from_table_category_list(
        ['PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST'],
        category_list
    )
    assert len(model.items) == 0
