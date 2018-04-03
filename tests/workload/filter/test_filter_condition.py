import datetime
from nwpc_hpc_model.workload.filter_condition import \
    FilterCondition, \
    get_property_data, \
    PropertyFilterCondition, \
    create_equal_value_checker, \
    create_greater_value_checker, \
    create_less_value_checker, \
    create_in_value_checker, \
    create_value_in_checker

from nwpc_hpc_model.workload import QueryItem, QueryProperty


def create_job_item_dict(
        job_id="id_no",
        owner="owner",
        job_class="job_class",
        queue_date=datetime.datetime.now(),
        status="R",
        priority=100,
        job_script="/script_path"
):
    return {
        "props": [
            {
                "id": "llq.id",
                "data": job_id,
                "text": job_id,
                "value": job_id
            },
            {
                "id": "llq.owner",
                "data": owner,
                "text": owner,
                "value": owner
            },
            {
                "id": "llq.class",
                "data": job_class,
                "text": job_class,
                "value": job_class
            },
            {
                "id": "llq.status" + job_id,
                "data": status,
                "text": status,
                "value": status
            },
            {
                "id": "llq.queue_date",
                "data": queue_date.strftime("%Y-%m-%d %H:%M:%S"),  # 2017-04-21 07:08:43
                "text": queue_date.strftime("%m/%d %H:%M"),  # "04/21 07:08",
                "value": queue_date.strftime("%a %b %d %H:%M:%S %Y"),  # "Fri Apr 21 07:08:43 2017"
            },
            {
                "id": "llq.priority",
                "data": priority,
                "text": priority,
                "value": priority
            },
            {
                "id": "llq.job_script",
                "data": job_script,
                "text": job_script,
                "value": job_script
            },
        ]
    }


def create_job_item(
        job_id="id_no",
        owner="owner",
        job_class="job_class",
        queue_date=datetime.datetime.now(),
        status="R",
        priority=100,
        job_script="/script_path"
):
    job_item = QueryItem()

    query_property = QueryProperty()
    query_property.map['id'] = "llq.job_id"
    query_property.map['text'] = job_id
    query_property.map['value'] = job_id
    query_property.map['data'] = job_id
    job_item.props.append(query_property)

    query_property = QueryProperty()
    query_property.map['id'] = "llq.owner"
    query_property.map['text'] = owner
    query_property.map['value'] = owner
    query_property.map['data'] = owner
    job_item.props.append(query_property)

    query_property = QueryProperty()
    query_property.map['id'] = "llq.class"
    query_property.map['text'] = job_class
    query_property.map['value'] = job_class
    query_property.map['data'] = job_class
    job_item.props.append(query_property)

    query_property = QueryProperty()
    query_property.map['id'] = "llq.queue_date"
    query_property.map['text'] = queue_date
    query_property.map['value'] = queue_date
    query_property.map['data'] = queue_date
    job_item.props.append(query_property)

    query_property = QueryProperty()
    query_property.map['id'] = "llq.status"
    query_property.map['text'] = status
    query_property.map['value'] = status
    query_property.map['data'] = status
    job_item.props.append(query_property)

    query_property = QueryProperty()
    query_property.map['id'] = "llq.status"
    query_property.map['text'] = str(priority)
    query_property.map['value'] = priority
    query_property.map['data'] = priority
    job_item.props.append(query_property)

    query_property = QueryProperty()
    query_property.map['id'] = "llq.job_script"
    query_property.map['text'] = job_script
    query_property.map['value'] = job_script
    query_property.map['data'] = job_script
    job_item.props.append(query_property)

    return job_item


def test_condition():
    condition = FilterCondition()
    job_item = dict()
    assert condition.is_fit(job_item)


def test_equal_value_checker():
    job_item = create_job_item_dict(job_id="id", owner="nwp_xp", job_class="serial", queue_date=datetime.datetime.now())

    condition = PropertyFilterCondition(
        property_id="llq.owner",
        data_checker=create_equal_value_checker("nwp_xp"))

    assert condition.is_fit(job_item)

    condition = PropertyFilterCondition(
        property_id="llq.owner",
        data_checker=create_equal_value_checker("unknown")
    )
    assert not condition.is_fit(job_item)


def test_greater_value_checker():
    job_item = create_job_item_dict(
        job_id="id",
        owner="nwp_xp",
        job_class="serial",
        queue_date=datetime.datetime.now(),
        priority=100
    )
    condition = PropertyFilterCondition(
        property_id="llq.priority",
        data_checker=create_greater_value_checker(50))

    assert condition.is_fit(job_item)

    condition = PropertyFilterCondition(
        property_id="llq.priority",
        data_checker=create_greater_value_checker(100)
    )
    assert not condition.is_fit(job_item)


def test_less_value_checker():
    job_item = create_job_item_dict(
        job_id="id",
        owner="nwp_xp",
        job_class="serial",
        queue_date=datetime.datetime.now(),
        priority=50
    )
    condition = PropertyFilterCondition(
        property_id="llq.priority",
        data_checker=create_less_value_checker(100))

    assert condition.is_fit(job_item)

    condition = PropertyFilterCondition(
        property_id="llq.priority",
        data_checker=create_less_value_checker(50)
    )
    assert not condition.is_fit(job_item)


def test_in_value_checker():
    job_item = create_job_item_dict(
        job_id="id",
        owner="nwp_xp",
        job_class="serial",
        queue_date=datetime.datetime.now(),
        priority=50
    )
    condition = PropertyFilterCondition(
        property_id="llq.owner",
        data_checker=create_in_value_checker(("nwp_xp", "nwp", "nwp_qu")))

    assert condition.is_fit(job_item)

    condition = PropertyFilterCondition(
        property_id="llq.owner",
        data_checker=create_in_value_checker(("unknown",))
    )
    assert not condition.is_fit(job_item)


def test_value_in_checker():
    job_item = create_job_item_dict(
        job_id="id",
        owner="nwp_xp",
        job_class="serial",
        queue_date=datetime.datetime.now(),
        priority=50,
        job_script="/cma/g3/test.ksh"
    )
    condition = PropertyFilterCondition(
        property_id="llq.job_script",
        data_checker=create_value_in_checker("g3")
    )

    assert condition.is_fit(job_item)

    condition = PropertyFilterCondition(
        property_id="llq.job_script",
        data_checker=create_value_in_checker("g2")
    )
    assert not condition.is_fit(job_item)
