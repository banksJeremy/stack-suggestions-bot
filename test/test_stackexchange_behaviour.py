import json

import pytest
from httmock import urlmatch, HTTMock

import stackexchange


def test_stackexchange_init_sites():
    """
    Tests that the StackExchange class will correctly initialize a list
    of Site objects based on a request to /sites, when instantiated.
    """
    with HTTMock(sites_returning_stackoverflow):
        stack_exchange = stackexchange.StackExchange()

        assert len(stack_exchange.sites) == 1

        with pytest.raises(ValueError):
            stack_exchange.get_site("this is a no\x00t a site")

        stack_overflow = stack_exchange.get_site("Stack Overflow")

        assert stack_overflow == stack_exchange.get_site('stackoverflow')

        assert stack_overflow.se == stack_exchange
        assert stack_overflow.name == "Stack Overflow"
        assert stack_overflow.site_type == 'main_site'
        assert stack_overflow.site_state == 'normal'


@urlmatch(netloc=r'^api\.stackexchange\.com$', path=r'^/2\.2/sites$')
def sites_returning_stackoverflow(url, request):
    return json.dumps({
        "items": [{
            "aliases": ["http://www.stackoverflow.com", "http://facebook.stackoverflow.com"],
            "styling": {
                "tag_background_color": "#E0EAF1",
                "tag_foreground_color": "#3E6D8E",
                "link_color": "#0077CC"
            },
            "related_sites": [{
                "relation": "meta",
                "api_site_parameter": "meta.stackoverflow",
                "site_url": "http://meta.stackoverflow.com",
                "name": "Meta Stack Overflow"
            }, {
                "relation": "chat",
                "site_url": "http://chat.stackoverflow.com",
                "name": "Stack Overflow Chat"
            }],
            "markdown_extensions": ["Prettify"],
            "launch_date": 1221436800,
            "site_state": "normal",
            "high_resolution_icon_url": "http://cdn.sstatic.net/stackoverflow/img/apple-touch-icon@2.png",
            "favicon_url": "http://cdn.sstatic.net/stackoverflow/img/favicon.ico",
            "icon_url": "http://cdn.sstatic.net/stackoverflow/img/apple-touch-icon.png",
            "audience": "professional and enthusiast programmers",
            "site_url": "http://stackoverflow.com",
            "api_site_parameter": "stackoverflow",
            "logo_url": "http://cdn.sstatic.net/stackoverflow/img/logo.png",
            "name": "Stack Overflow",
            "site_type": "main_site"
        }],
        "has_more": True,
        "quota_max": 300,
        "quota_remaining": 273
    })
