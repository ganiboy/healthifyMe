class ValidationError(Exception):
    def __init__(self, msg, status_code):
        self.msg = msg
        self.status_code = status_code


class KeyError(Exception):
    def __init__(self, msg, status_code):
        self.msg = msg
        self.status_code = status_code