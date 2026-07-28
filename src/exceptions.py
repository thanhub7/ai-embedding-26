class ConnectionError(Exception):
    pass

class TimeoutError(Exception):
    pass

class HTTPError(Exception):
    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code

class BadRequestError(HTTPError):
    def __init__(self, message="Bad Request"):
        super().__init__(400, message)

class UnauthorizedError(HTTPError):
    def __init__(self, message="Unauthorized"):
        super().__init__(401, message)

class ForbiddenError(HTTPError):
    def __init__(self, message="Forbidden"):
        super().__init__(403, message)

class NotFoundError(HTTPError):
    def __init__(self, message="Not Found"):
        super().__init__(404, message)

class InternalServerError(HTTPError):
    def __init__(self, message="Internal Server Error"):
        super().__init__(500, message)