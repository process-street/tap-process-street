import requests
import singer

from tap_process_street.constant import LIMIT_PARAM, AFTER_UPDATED_DATE_PARAM, AFTER_ID_PARAM

LOGGER = singer.get_logger()

""" Client for ProcessStreet API. """


class ProcessStreet(object):

    def __init__(self, api_key, domain, page_size):
        self.api_key = api_key
        self.uri = domain
        self.page_size = page_size

    def sync_stream(self, path, paramArgs=None):
        uri = "{uri}/{path}".format(uri=self.uri, path=path)

        has_more = True
        params = {
            LIMIT_PARAM: self.page_size,
            AFTER_UPDATED_DATE_PARAM: paramArgs['last_updated_date'],
            AFTER_ID_PARAM: paramArgs['last_id']
        }

        while has_more:
            LOGGER.info("GET request to {uri} {params}".format(uri=uri, params=params))
            response = requests.get(uri, stream=True, headers={"x-api-key": self.api_key}, params=params)
            response.raise_for_status()

            json = response.json()
            has_more = json['hasMore']
            data = json['data']

            if has_more:
                params = {
                    LIMIT_PARAM: self.page_size,
                    AFTER_UPDATED_DATE_PARAM: json['nextPageUpdatedDate'],
                    AFTER_ID_PARAM: json['nextPageId']
                }

            yield data
