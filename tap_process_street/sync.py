import singer

from tap_process_street.client import ProcessStreet

LOGGER = singer.get_logger()

def sync(config, state, catalog):
    client = ProcessStreet(**config)

    for stream in catalog.get_selected_streams(state):
        tap_stream_id = stream.tap_stream_id
        LOGGER.info("Syncing stream:" + tap_stream_id)

        singer.write_schema(
            stream_name=tap_stream_id,
            schema=stream.schema.to_dict(),
            key_properties=stream.key_properties,
        )

        params = {
            'last_updated_date': singer.get_bookmark(state, tap_stream_id, 'last_updated_date'),
            'last_id': singer.get_bookmark(state, tap_stream_id, 'last_id'),
        }

        with singer.metrics.record_counter(tap_stream_id) as counter:
            for page in client.sync_stream(tap_stream_id, params):
                for item in page:
                    singer.write_records(tap_stream_id, [item])

                    state = singer.write_bookmark(state, tap_stream_id, 'last_updated_date', item['updatedDate'])
                    state = singer.write_bookmark(state, tap_stream_id, 'last_id', item['id'])
                    singer.write_state(state)
                    counter.increment()

    return
