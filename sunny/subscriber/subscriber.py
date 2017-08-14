"""
This is the base subscriber of the any type of data stream like zeromq,csv files,raw sockets
"""
class BaseSubscriber(object):
    TYPE_OF_SUBSCRIPTION = None

    def get_publisher(self):
        """
        Stores the information of who is publishing the data for example CSV file, socket infos etc
        """
        raise NotImplementedError()
    def get_subscriber(self):
        """
        returns the subscriber object
        """
        raise NotImplementedError()
    def set_filters(self , filter_object = None):
        """
        Stores the filters info for the subscriber
        """
        raise NotImplementedError()

    def add_filter(self ,filter_object = None):
        """
        To add another filter on the streamed data
        """
        raise NotImplementedError()
    def add_publisher(self , publisher_object = None):
        """
        To add another publisher for the streaming data
        """
        raise NotImplementedError()


