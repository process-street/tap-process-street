import logging

import requests

logger = logging.getLogger()

""" Simple wrapper for ProcessStreet. """


class ProcessStreet(object):

    def __init__(self, api_key, domain):
        self.api_key = api_key
        self.uri = domain

    def get(self, path, stream=True, **kwargs):
        uri = "{uri}{path}".format(uri=self.uri, path=path)
        logger.info("GET request to {uri}".format(uri=uri))

        response = requests.get(uri, stream=stream, headers={"x-api-key": self.api_key})
        response.raise_for_status()

        yield response.json()

    #
    # Methods to retrieve data per stream/resource.
    #
    def checklists(self):
        for i in self.get("/checklists"):
            for j in i:
                yield j
