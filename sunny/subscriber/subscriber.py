"""
This is the base subscriber of the any type of data stream like zeromq,csv files,raw sockets
"""
class BaseSubscriber(object):
    TYPE_OF_SUBSCRIPTION = None

    def get_publisher():
        """
        Stores the information of who is publishing the data for example CSV file, socket infos etc
        """
        raise NotImplementedError()
    def get_subscriber():
        """
        returns the subscriber object
        """
        raise NotImplementedError()
    def set_filters():
        """
        Stores the filters info for the subscriber
        """
        raise NotImplementedError()


