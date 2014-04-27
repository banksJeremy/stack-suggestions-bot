import pytest

import stackexchange
from stackexchange.errors import (
    APIError, BadParameter, ThrottleViolation)

from mock_responses import (
    only_httmock,
    sites_returning_stackoverflow, throttle_violation_for_questions)


def test_apierror_factory_constructs_correct_classes():
    """
    Confirms that the APIError factory creates instances of the right type.
    """

    bad_param_error = APIError.from_response_data({
        "error_id": 400,
        "error_message": "sort",
        "error_name": "bad_parameter"
    })

    assert type(bad_param_error) is BadParameter


    throttle_violation = APIError.from_response_data({
        "error_id": 502,
        "error_message": "too many requests from this IP, more requests available in 65127 seconds",
        "error_name": "throttle_violation"
    })

    assert type(throttle_violation) is ThrottleViolation


    unknown_error = APIError.from_response_data({
        "error_id": 9135146,
        "error_message": "FAKE",
        "error_name": "FAKE"
    })

    assert type(unknown_error) is APIError


def test_api_errors_raised():
    """
    Confirms that error responses from the API result in raised APIErrors.
    """

    with only_httmock(
        sites_returning_stackoverflow,
        throttle_violation_for_questions
    ):
        stack_exchange = stackexchange.StackExchange()

        with pytest.raises(ThrottleViolation):
            stack_exchange._request('questions', site='stackoverflow')
