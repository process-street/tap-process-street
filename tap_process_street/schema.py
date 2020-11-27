import json
import os

STREAMS = [
    'approvals',
    'checklists',
    'form-field-values',
    'form-field-widgets',
    'tasks',
    'templates',
    'users'
]


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def get_schemas():
    schemas = {}

    for stream_name in STREAMS:
        schema_path = get_abs_path('schemas/{}.json'.format(stream_name))

        with open(schema_path) as file:
            schema = json.load(file)

        schemas[stream_name] = schema

    return schemas
