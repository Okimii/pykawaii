__all__ = ["WaifupyBaseException", "CacheDisabled"]

class WaifupyBaseException(Exception):
    def __init__(self, message: str, /) -> None:
        super().__init__(message)

class CacheDisabled(WaifupyBaseException):
    super().__init__("The client's cache is disabled.")