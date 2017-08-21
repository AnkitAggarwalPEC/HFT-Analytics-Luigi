import queue_subscriber

class FunctionNotSupported(Exception):
    """
    Raise this exception when the function doesn't make sense
    """
    pass

class PublisherNotSane(Exception):
    """
    Raise this exception when the publisher is not sane
    """
    pass
class PublisherOfDifferentType(Exception):
    """
    This is raised when there is mismatch of publisher type
    """
    pass

class ZMOSubscriber(queue_subscriber.QueueSubscriber):
    QUEUE_TYPE =  ZM_QUEUE
    def __init__(self , publisher_object = None , filter_object = None):
        """
        This publisher belong to zeromq publisher
        """
        self.publisher_object = publisher_object
        self._publisher_object_list = []
        if publisher_object is not None:
            self._publisher_object_list.append(publisher_object)
        self.filter_object =  filter_object


    def insert(self , data_to_be_inserted = None , index_list = None):
        """
        This cannot be supported as it is stream read
        """
        raise FunctionNotSupported("This is not valid for streaming data")


    def pop(self , index_list = None ):
        """
        This will pop the top data  from all the publisher unless a index list is provided
        """
        _index_list = index_list if index_list in not None else range(len(self._publisher_object_list))


    def peek(self , index_list = None):
        """
        This will return the top data from all the publisher unless a index list is provided
        """
        _data = []
        _index_list = index_list if index_list in not None else range(len(self._publisher_object_list))



    def full(self , index_list = None):
        """
        This is not supported for the streaming data
        """
        raise FunctionNotSupported("This is not supported from streaming data")

    def register_publisher(self , publisher_object = None ):
        if publisher_object is None:
            raise PublisherNotSane("This publisher is not sane")
        else if publisher_object.TYPE is not QUEUE_TYPE:
            raise PublisherOfDifferentType("Check the publisher you are queuing")
        self._publisher_object_list.append(publisher_object)

    def add_publisher(self , publisher_object = None):
        if publisher_object is None:
            raise PublisherNotSane("This publisher is not sane")
        else if publisher_object.TYPE is not QUEUE_TYPE:
            raise PublisherOfDifferentType("Check the publisher you are queuing")
        self._publisher_object_list.append(publisher_object)

