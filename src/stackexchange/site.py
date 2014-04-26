class Site(object):
    def __init__(self, stack_exchange, site_data):
        """
        Initializes the Site given a item from a /sites response.

        The data must be complete; don't filter out any fields.
        (The default behaviour is to include all fields.)

        The Site objet will have all possible fields from the /sites
        response as attributes. Omitted optional fields will either be
        None, or an empty array (if a present value would be an array).
        """
        self.se = stack_exchange
        self._dict = site_data

        self.name = site_data['name']
        self.api_site_parameter = site_data['api_site_parameter']
        self.site_url = site_data['site_url']
        self.aliases = site_data.get('aliases') or []

        self.audience = site_data['audience']
        self.closed_beta_date = site_data.get('closed_beta_date')
        self.favicon_url = site_data['favicon_url']
        self.icon_url = site_data['icon_url']
        self.high_resolution_icon_url = site_data.get('high_resolution_icon_url')
        self.launch_date = site_data.get('launch_date')
        self.logo_url = site_data['logo_url']
        self.markdown_extensions = site_data.get('markdown_extensions') or []
        self.open_beta_date = site_data.get('open_beta_date')
        self.related_sites = site_data.get('related_sites') or []
        self.site_state = site_data['site_state']
        self.site_type = site_data['site_type']
        self.styling = site_data['styling']
        self.twitter_account = site_data.get('twitter_account')

    def _request(self, path, object_hook=None, **kwargs):
        return self.se._request(
            path, self.api_site_parameter, object_hook, **kwargs)

    def get_similar(self, title, preferred_tags=None, excluded_tags=None):
        """
        Requests some questions similar to a title.
        """
        params = {
            'title': title,
            'sort': 'relevance',
            'page': 1,
            'page_size': 25,
            'tagged': ';'.join(preferred_tags or []),
            'nottagged': ';'.join(excluded_tags or [])
        }

        return self._request('similar', **params)['items']
