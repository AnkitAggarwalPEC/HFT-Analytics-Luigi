"""
A class for handling the elasticsearch as the index
"""

class ElasticSearchSink(Sink):


    marker_index = "update_log" # This will be used for the logging purpose
    marker_doc_type = "entry"   # This is the doc type
    #TODO : To read from the confriguration
    def __init__(self , host , port , index , doc_type , update_id ,marker_index_hist_size = 0 , http_auth = None, timeout = 10 , extra_elastic_args = {}):
        self.host = host
        self.port = port
        self.http_auth = http_auth
        self.index = index
        self.doc_type = doc_type
        self.update_id = update_id
        self.marker_index_hist_size = marker_index_hist_size
        self.timeout = timeout
        self.extra_elastic_args = extra_elastic_args

        self.es = elasticsearch.Elasticsearch(
                host = self.host,
                port = self.port,
                http_auth = self.http_auth,
                timeout = self.timeout
                **extra_elastic_args
                )
    def marker_index_document_id(self):
        """
        This will return the id for the marker index
        """
        params = '%s:%s:%s' % (self.index, self.doc_type, self.update_id)
        return hashlib.sha1(params.encode('utf-8')).hexdigest()

    def create_marker_index(self):
        """
        This is to create the marker index
        """
        if not.self.es.indices.exists(index = self.marker_index):
            self.es.indices.create(index = self.marker_index)

    def update_marker_index(self):
        """
        This is used to update the marker index for the logging purpose
        """
        self.create_marker_index()
        self.ex.index(index = self.marker_index , doc_type = self.marker_doc_type , id = self.marker_index_document_id() , body = {
            'update_id' : self.update_id,
            'target_index' : self.index ,
            'target_doc_type' : self.doc_type,
            'date' : datetime.datetime.now()})
        self.es.indices.flush(index = self.marker_index)

    def exists(self):
        """
        Check, if the task has been runned
        """
        try:
            self.es.get(index = self.marker_index , doc_type = self.marker_doc_type ,id = self.marker_index_document_id())
            return True
        except elasticsearch.NotFoundError:
            pass
        except elasticsearch.ElasticsearchException as err:
            pass
        return False

