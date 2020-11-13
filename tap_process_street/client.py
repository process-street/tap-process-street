import requests
import singer

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
            'limit': self.page_size,
            'afterUpdatedDate': paramArgs['last_updated_date'],
            'afterId': paramArgs['last_id']
        }

        LOGGER.info("GET request to {uri} {params}".format(uri=uri, params=params))

        while has_more:
            response = requests.get(uri, stream=True, headers={"x-api-key": self.api_key}, params=params)
            response.raise_for_status()

            json = response.json()
            has_more = json['hasMore']
            data = json['data']

            if has_more:
                params = {
                    'limit': self.page_size,
                    'afterUpdatedDate': json['nextPageUpdatedDate'],
                    'afterId': json['nextPageId'],
                }

            yield data
