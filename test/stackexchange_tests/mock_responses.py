import json

import httmock


def only_httmock(*mocks):
    """
    Wraps a typical HTTPMock context manager to raise an error if no mocks match.
    """
    mocks = mocks + (fail_everything_else,)
    return httmock.HTTMock(*mocks)


@httmock.urlmatch(netloc=r'^api\.stackexchange\.com$', path=r'^/2\.2/sites$')
def sites_returning_stackoverflow(url, request):
    """
    A response for a /sites request; accurate except that it indicates
    that Stack Overflow is the only site on the network (despite
    referring to others in related_sites).
    """

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
        "has_more": False,
        "quota_max": 300,
        "quota_remaining": 273
    })


@httmock.urlmatch(netloc=r'^api\.stackexchange\.com$', path=r'^/2\.2/questions')
def throttle_violation_for_questions(url, request):
    return json.dumps({
        "error_id": 502,
        "error_message": "too many requests from this IP, more requests available in 65127 seconds",
        "error_name": "throttle_violation"
    })


@httmock.urlmatch(netloc=r'.*')
def fail_everything_else(url, request):
    raise Exception("unexpected request; no mock available", request)

