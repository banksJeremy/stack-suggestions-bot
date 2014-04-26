import json

import requests

from .site import Site
from .errors import APIError


class StackExchange(object):
    """
    A simple wrapper for the Stack Exchange API V2.2.

    This doesn't consider rate limiting or any important things like
    that. Careless use could result in being blocked.

    This doesn't support the use of filters which remove API fields
    that are present by default.
    """

    API_ROOT = 'http://api.stackexchange.com/2.2/'

    def __init__(self, key=None):
        self._key = key

        self._init_sites_list()

    def _init_sites_list(self):
        sites_data = self._request('sites', pagesize=99999)

        sites = {}

        for site_data in sites_data:
            site = Site(self, site_data)
            sites[site.api_site_parameter] = site

        # maps from site API identifiers to Site objects
        self.sites = sites

    def _request(self, path, site=None, object_hook=None, **kwargs):
        url = self.API_ROOT + path

        params = dict(kwargs)

        # The "unsafe" mode returns data correctly encoded, instead of
        # protectively over-encoded. That's the main reason we're using
        # it, although also includes many (all?) fields that aren't
        # included by default. Ideally, we may want to create a custom
        # filter returning what we actually know how to use.
        params['filter'] = 'unsafe'

        if site:
            params['site'] = site

        if self._key:
            params['key'] = self._key

        response = requests.get(url, params=params, stream=True)

        response_data = json.loads(response.text, object_hook=object_hook)

        if 'error_id' in response_data:
            raise APIError.from_response_data(response_data)
        else:
            return APIItems.from_response_data(response_data)

    def get_site(self, identifier):
        """
        Returns a Site object given a site's domain, name, slug, or ID.
        """

        # if given the api identifier, we can get it instantly
        if identifier in self.sites:
            return self.sites[identifier]

        # otherwise we need to search for it
        for site in self.sites.values():
            if identifier == site.name:
                return site

            if identifier == site.site_url:
                return site

            if identifier in site.aliases:
                return site

        raise ValueError("no site found matching %r" % (identifier,))


class APIItems(list):
    """
    A list of items from an API response, with API metadata attached.
    """
    @staticmethod
    def from_response_data(response_data):
        self = APIItems(response_data['items'])

        self._response_data = response_data

        self.has_more = response_data['has_more']

        self.backoff = response_data.get('backoff', 0)
        self.quota_max = response_data['quota_max']
        self.quota_remaining = response_data['quota_remaining']

        return self
