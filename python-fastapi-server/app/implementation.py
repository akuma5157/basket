"""basket API implementation
"""
from datetime import datetime


class Implementation():
    # get_time -- Synchronisation point for meld
    @staticmethod
    def get_time(*args, **kwargs):
        """
        :param request: An HttpRequest
        """
        return datetime.now().isoformat()

