import pytest
import copy

from nwpc_hpc_model.workload.loadleveler import query_category, value_saver
from nwpc_hpc_model.workload.loadleveler import record_parser


class TestQueryCategory:
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_deep_copy(self):
        category = query_category.QueryCategory()
        category.id = "llq.id"
        category.record_parser = record_parser.DetailLabelParser("Job Step Id")
        category.value_saver = value_saver.StringSaver()

        new_category = copy.deepcopy(category)
        new_category.id = "llq.submitted"
        new_category.record_parser.label = "Submitted"

        assert category.id != new_category.id
        assert category.record_parser is not new_category.record_parser
        assert category.record_parser.label is not new_category.record_parser.label

    def test_create_query_category(self):
        id_category = query_category.QueryCategory(
            category_id="llq.id",
            display_name="Id",
            label="Job Step Id",
            record_parser_class=record_parser.DetailLabelParser,
            record_parser_arguments=("Job Step Id",),
            value_saver_class=value_saver.StringSaver
        )

        assert id_category.id == "llq.id"
        assert id_category.display_name == "Id"
        assert id_category.label == "Job Step Id"
        assert isinstance(id_category.record_parser, record_parser.DetailLabelParser)
        assert id_category.record_parser.label == "Job Step Id"
        assert isinstance(id_category.value_saver, value_saver.StringSaver)

    def test_llq_detail_category_list(self):
        category_list = query_category.QueryCategoryList()

        category_list.extend([
            query_category.QueryCategory("llq.id",          "Id",           "Job Step Id",
                                         record_parser.DetailLabelParser, ("Job Step Id",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.owner",       "Owner",        "Owner",
                                         record_parser.DetailLabelParser, ("Owner",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.class",       "Class",        "Class",
                                         record_parser.DetailLabelParser, ("Class",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.job_script",  "Job Script",   "Cmd",
                                         record_parser.DetailLabelParser, ("Cmd",),
                                         value_saver.StringSaver, ()),
            query_category.QueryCategory("llq.status",      "Status",       "Status",
                                         record_parser.DetailLabelParser, ("Status",),
                                         value_saver.JobStatusSaver, ())
        ])

        assert len(category_list) == 5

        assert category_list.index_from_id("llq.id") == 0

        with pytest.raises(ValueError):
            category_list.index_from_id("llclass.id")

        assert category_list.contains_id("llq.id")
        assert not category_list.contains_id("llclass.id")
        assert category_list.category_from_id("llq.id").id == "llq.id"
        assert category_list.category_from_id("llclass.id") is None

        assert category_list.index_from_label("Class") == 2
        assert category_list.contains_label("Class")
        assert category_list.category_from_label("Class").id == "llq.class"
