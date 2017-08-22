import filters

class ZMQFilter(filters.BaseFilter):

    def __init__(self , socket_object = None , topic_filters = None , should_contain = None , should_not_contain = None ):
        self.socket_object = socket_object
        self.topic_filters = topic_filters
        self.should_contain = should_contain
        self.should_not_contain = should_not_contain
        self._filter_reseted = False

    def get_filter(self):
        return dict({"topic_filter" :  self.topic_filters , "should_contain" : self.should_contain , "should_not_contain" : self.should_not_contain})

    def reset_filter(self):
        self.topic_filters = None
        self.should_contain = None
        self.should_not_contain = None
        self._filter_reseted = True

    def _set_topic_filter(self , filter_topic = None):
        self.topic_filters = filter_topic

    def _get_topic_filters(self):
        return self.topic_filters

    def _set_should_contain(self , should_contain =  None):
        self.should_contain = should_contain

    def _get_should_contain(self):
        return should_contain

    def _set_should_not_contain(self, should_not_contain = None):
        self.should_not_contain = should_not_contain

    def _get_should_not_contain(self):
        return self.should_not_contain

    def add_filter(self ,topic_filters = None ,  should_contain = None , should_not_contain= None):

