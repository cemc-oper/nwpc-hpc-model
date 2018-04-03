# coding=utf-8
from nwpc_hpc_model.workload.filter import Filter


def test_filter():
    a_filter = Filter()
    job_items = [
        {},
        {}
    ]

    target_job_items = a_filter.filter(job_items)

    assert job_items == target_job_items
