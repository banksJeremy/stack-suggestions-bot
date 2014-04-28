import pytest

from stackexchange.stackexchange import APIItems

from mock_responses import THREE_SO_BADGES_WRAPPED


def test_apiitems():
    """
    Verifies that APIItems is correctly constructed with some data and metadata.
    """
    items = APIItems.from_response_data(THREE_SO_BADGES_WRAPPED)

    assert isinstance(items, APIItems)
    assert len(items) == 3
    assert items[0]['name'] == 'cryptography'
    assert items[2]['badge_id'] == 265

    # present metadata
    assert items.has_more == True
    assert items.quota_remaining == 9913
    assert items.quota_max == 10000

    # absent metadata, default value
    assert items.backoff == 0
