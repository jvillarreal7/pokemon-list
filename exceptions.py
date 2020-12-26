class Error(Exception):
    """Base class for other exceptions"""
    pass

class GensLowerThanOneError(Error):
    """Raised when the input value for gens is less than 1."""
    pass

class StartGenHigherThanEndGenError(Error):
    """Raised when the input value for start gen is higher than end gen."""
    pass

class UnsupportedGenError(Error):
    """Raised when the input value for either gen is not defined."""
    pass