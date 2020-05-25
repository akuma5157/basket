"""basket API implementation
"""
from .stubs import AbstractStubClass
from datetime import datetime


class Implementation(AbstractStubClass):
    # getTime -- Synchronisation point for meld
    @staticmethod
    def getTime(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        return datetime.now().isoformat()
