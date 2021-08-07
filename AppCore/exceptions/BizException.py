
class BizException(Exception):
    """Exception raised for errors in the wrong business
    Attributes:
        code -- code of exception
        message -- explanation of the error
    """
    code = ''
    message = ''

    def __init__(self, code, message='Business Exception'):
        super().__init__(self, message)
        self.message = message
        self.code = code
