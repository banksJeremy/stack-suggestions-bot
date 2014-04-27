import pytest

import stackexchange

from .mock_responses import only_httmock, sites_returning_stackoverflow


def test_stackexchange_init_sites():
    """
    Tests that the StackExchange class will correctly initialize a list
    of Site objects based on a request to /sites, when instantiated.
    """
    with only_httmock(sites_returning_stackoverflow):
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
