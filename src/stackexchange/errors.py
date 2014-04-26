class APIError(Exception):
    @staticmethod
    def from_response_data(response_data):
        """
        Returns an instance of APIError or a more specific subclass,
        from the error information in the given JSON response data.
        """

        error_id = response_data['error_id']

        if error_id == 400:
            cls = BadParameter
        elif error_id == 502:
            cls = ThrottleViolation
        else:
            cls = APIError

        return cls(response_data)

    def __init__(self, response_data):
        self._response_data = response_data

        super(APIError, self).__init__(
            "{error_name} ({error_id}): {error_message}".format(**response_data))


class BadParameter(APIError):
    pass


class ThrottleViolation(APIError):
    pass
