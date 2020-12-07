from singer import metadata
from singer.catalog import Catalog, CatalogEntry, Schema

from tap_process_street.schema import get_schemas, STREAMS


def discover():
    streams = []
    for schema_name, schema_dict in get_schemas().items():
        schema = Schema.from_dict(schema_dict)
        schema_meta = metadata.get_standard_metadata(
            schema=schema_dict,
            schema_name=schema_name,
            key_properties=STREAMS[schema_name]['key_properties'],
            valid_replication_keys=STREAMS[schema_name]['replication_keys'],
            replication_method=STREAMS[schema_name]['replication_method']
        )

        streams.append(
            CatalogEntry(
                tap_stream_id=schema_name,
                stream=schema_name,
                schema=schema,
                key_properties=STREAMS[schema_name]['key_properties'],
                metadata=schema_meta,
            )
        )
    return Catalog(streams)
