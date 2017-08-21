import subscriber
"""
This is the base class for managing the queue based subcsriber like zeromq, apache kafka, rabbitmq
"""

class QueueSubscriber(subscriber.BaseSubscriber):
    QUEUE_TYPE = None

    def get_list_of_queues_supported():
        """
        This returns the list of the queue based supported
        Future scope is that this list will be updated
        """
        return ["PYTHON_BASIC_QUEUE", "PYTHON_PRIORITY_QUEUE" , "ZEROMQ"]

    def insert(self , data_to_be_inserted = None):
        """
        This method is to use to insert the data in the queue used
        """
        raise NotImplementedError()

    def pop(self):
        """
        This is pop the data from the queue
        """
        raise NotImplementedError()

    def peek(self):
        """
        This is to peek the top data present in the queue
        """
        raise NotImplementedError()

    def full(self):
        """
        This is to check whether the queue is filled
        """
        raise NotImplementedError()

    def register_publisher(self , publisher_object = None):
        """
        This to register the publisher with the subscriber
        """
        raise NotImplementedError()

    def add_publisher(self , publisher_object = None):
        """
        This is add to the list of existing publisher
        """
        raise NotImplementedError()


