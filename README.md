# nwpc-hpc-model

[![Build Status](https://travis-ci.org/perillaroc/nwpc-hpc-model.svg?branch=master)](https://travis-ci.org/perillaroc/nwpc-hpc-model)
[![codecov](https://codecov.io/gh/perillaroc/nwpc-hpc-model/branch/master/graph/badge.svg)](https://codecov.io/gh/perillaroc/nwpc-hpc-model)

A key-value model for HPC resources in NWPC. Including models for:

* LoadLeveler's `llq -l` query
* Slurm's `sinfo` and `squeue -o %all` query
* Disk usage and disk space query

## Installation

Download source code from Github releases or get the latest code from Github repo. 

Run `pip install .` to install.

## Getting started

The following example uses `nwpc-hpc-model` to extract job id and job owner from a `llq -l` query.
 
A config YAML file is used to create query categories.

```yaml
category_list:
  -
    id: "llq.id"
    display_name: "Id"
    label: "Job Step Id"
    record_parser_class: "DetailLabelParser"
    record_parser_arguments:
      - "Job Step Id"
    value_saver_class: "StringSaver"
    value_saver_arguments: []
  -
    id: "llq.owner"
    display_name: "Owner"
    label: "Owner"
    record_parser_class: "DetailLabelParser"
    record_parser_arguments:
      - "Owner"
    value_saver_class: "StringSaver"
    value_saver_arguments: []

```

First create `QueryCategoryList` according to the config json file.

```python
from nwpc_hpc_model.workload.loadleveler import QueryCategoryList, \
    QueryCategory, record_parser, value_saver
import yaml

with open('config_file_path', 'r') as f:
    config = yaml.load(f)
    
category_list = QueryCategoryList()
for an_item in config['category_list']:
    category = QueryCategory(
        category_id=an_item['id'],
        display_name=an_item['display_name'],
        label=an_item['display_name'],
        record_parser_class=getattr(record_parser, an_item['record_parser_class']),
        record_parser_arguments=tuple(an_item['record_parser_arguments']),
        value_saver_class=getattr(value_saver, an_item['value_saver_class']),
        value_saver_arguments=tuple(an_item['value_saver_arguments'])
    )
    category_list.append(category)
```

Get `llq -l` command output.

```python
import subprocess

command = "/usr/bin/llq -l"
pipe = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
output = pipe.communicate()[0]
output_string = output.decode()
output_lines = output_string.split("\n")
```

Build `QueryModel` from `QueryCategoryList`

```python
from nwpc_hpc_model.workload.loadleveler import LoadLevelerQueryModel

model = LoadLevelerQueryModel.build_from_category_list(output_lines, category_list)
```

`model` contains data of all categories in the config file.

## Test

Use `pytest` to run all tests.

## License

Copyright &copy; 2016-2019, Perilla Roc.

`nwpc-hpc-model` is licensed under [The MIT License](https://opensource.org/licenses/MIT).
