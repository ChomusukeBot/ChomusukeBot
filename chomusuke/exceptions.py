class ChomusukeException(Exception):
    """
    Base exception for all of Chomusuke's problems.
    """


class FeatureRequired(ChomusukeException):
    """
    Exception raised when a specific Bot feature is required by a Cog.
    """


class WebServerRequired(FeatureRequired):
    """
    Exception raised when a Cog requires the Sanic Web Server but is not available or is disabled.
    """
