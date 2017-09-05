#TODO:Create a config for the batch duration process
#Import the Publisher Context
#Import the connector module
"""
This is class handling all the connection objects
"""
from util import file_utils
class SinkNotSane(Exception):
    """
    Raise this when the Sink object is not a proper one
    """
    pass

class StreamingContext(object):
    """
    Main entry point for the Streaming fuctionality.It will be use for the interacting with the data we are recieving
    """
    _active_context = None
    def __init__(self , sink = None , batch_duration=None):
        """
        Create the new Streaming Context
        @param sink :: Sink for the published data
        @param batch_duration :: the time interval at which data will be divided
        """
        self._sink = self.intialize_sink(sink)
        self._batch_duration = batch_duration or self._default_batch_duration()
        self._active_context = self

    def _default_batch_duration(self):
        if file_utils.check_if_file_present(CONFIG_PATH):
            # TODO:READ THE CONFIG FILE FOR THE TIME
            pass
        else:
            """
            return the default 5 seconds
            """
            return 5

    def _intialize_sink(self, sink = None):
        if sink and sink.is_sane():
            return Sink.get_sink_object(sink)
        else:
            #TODO:Create the error
            raise SinkNotSane("Recheck the publisher object")

    @classmethod
    def get_active_context(cls , recreate_if_dead = None):
        """
        This will check if there is context is present live
        @param recreate_if_dead:To reintialize the context object
        """
        #TODO:Implement a way to get the running context
        pass

    def run_till_termination_or_timeout(self , timeout = None , data_points = None):
        """
        Stream the data to the subscriber till the data ran out or number of data points
        @param timeout = Time is seconds
        @param data_points = Number of data_points to be read
        """
        self._sink.timeout = timeout
        self._sink.data_points = data_points

    def stop(self ,stop_publisher=True):
        """
        This will stop the data to be transmitted to the subsriber
        @param stop_publisher = Stop the publisher too rather than keep reading
        @param stop_grace_fully
        """
        self._publisher_context.stop(stop_publisher)
        StreamingContext._active_context = None
        self._clean_up()

    def _clean_up(self):
        #TODO: to implement a way to clean up the publisher and subscriber
        pass

    def socket_stream(self, hostname , port , data_transformer = None , connector = None, filter_object = None ):
        """
        This will create the socket stream for the given hostname and port
        @param hostname
        @param port
        @data_transformer  Datatransformer object for the data recieved
        @connector connector object whether raw socket or pyzmq
        @filter_object = To filter the data after transformation
        """
        #Create a stream subscriber for the data
        #TODO: Create a connector accordingly to the connector
        pass
    def text_file_stream(self, file_path , data_transformer , stream_policy = None , lines_to_read = None , filter_object = None) :
        """
        This will create the text file stream from the given location
        @param file_path = location of the text file
        @param data_transformer To transform the data from one type to another
        @param stream_policy : To tail the file or read whole
        @param lines_to_read : To tell number of lines to be read
        @param filter_object : To filter the data after transformation
        """
        pass
        #TODO:Create a text_file_stream

    def add_another_stream(self, stream_object):
        """
        This will add the another streaming to the list of the streamers writing to sink
        """
        pass











