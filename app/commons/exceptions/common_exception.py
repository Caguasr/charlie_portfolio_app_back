from typing import Any


class CommonException(Exception):
    def __init__(self, message: Any, code: int):
        self.message = message
        self.code = code
