"""
This is the base publisher for the different type of subscriber
"""
class BasePubliser(object):
    TYPE_OF_SUBSCRIPTION = None

    def get_publisher(self):
        """
        This is to get the raw publisher object
        """
        raise NotImplementedError()


