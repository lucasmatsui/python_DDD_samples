class InvalidEmailError(Exception):
    def __init__(self, message):
        self.message = message
        self.status_code = 400
