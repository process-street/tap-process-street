from singer import metadata
from singer.catalog import Catalog, CatalogEntry, Schema

from tap_process_street.constant import UPDATED_DATE_KEY, ID_KEY
from tap_process_street.schema import get_schemas


def discover():
    streams = []
    for schema_name, schema_dict in get_schemas().items():
        schema = Schema.from_dict(schema_dict)
        schema_meta = metadata.get_standard_metadata(
            schema=schema_dict,
            schema_name=schema_name,
            key_properties=[ID_KEY],
            valid_replication_keys=[UPDATED_DATE_KEY, ID_KEY],
            replication_method='INCREMENTAL'
        )

        streams.append(
            CatalogEntry(
                tap_stream_id=schema_name,
                stream=schema_name,
                schema=schema,
                key_properties=[UPDATED_DATE_KEY, ID_KEY],
                metadata=schema_meta,
            )
        )
    return Catalog(streams)
