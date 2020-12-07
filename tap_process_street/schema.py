import json
import os

from tap_process_street.constant import ID_KEY, UPDATED_DATE_KEY, UPDATED_OR_MIGRATED_DATE_KEY

STREAMS = {
    'approvals': {
        'key_properties': [ID_KEY],
        'replication_method': 'INCREMENTAL',
        'replication_keys': [UPDATED_DATE_KEY, ID_KEY]
    },
    'checklists': {
        'key_properties': [ID_KEY],
        'replication_method': 'INCREMENTAL',
        'replication_keys': [UPDATED_DATE_KEY, ID_KEY]
    },
    'form-fields': {
        'key_properties': [ID_KEY],
        'replication_method': 'INCREMENTAL',
        'replication_keys': [UPDATED_DATE_KEY, ID_KEY]
    },
    'form-field-values': {
        'key_properties': [ID_KEY],
        'replication_method': 'INCREMENTAL',
        'replication_keys': [UPDATED_OR_MIGRATED_DATE_KEY, ID_KEY]
    },
    'tasks': {
        'key_properties': [ID_KEY],
        'replication_method': 'INCREMENTAL',
        'replication_keys': [UPDATED_OR_MIGRATED_DATE_KEY, ID_KEY]
    },
    'task-templates': {
        'key_properties': [ID_KEY],
        'replication_method': 'INCREMENTAL',
        'replication_keys': [UPDATED_DATE_KEY, ID_KEY]
    },
    'templates': {
        'key_properties': [ID_KEY],
        'replication_method': 'INCREMENTAL',
        'replication_keys': [UPDATED_DATE_KEY, ID_KEY]
    }
}


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def get_schemas():
    schemas = {}

    for stream_name in STREAMS.keys():
        schema_path = get_abs_path('schemas/{}.json'.format(stream_name))

        with open(schema_path) as file:
            schema = json.load(file)

        schemas[stream_name] = schema

    return schemas
