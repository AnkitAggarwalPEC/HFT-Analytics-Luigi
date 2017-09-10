class BaseIOStream(object):
    """
    A class to write to and read from a file or socket
    """
    def __init__(self , stream_object , *args , **kwargs):

    def read_until_regex(self , regex ):
        pass
    def read_until():
        pass
    def read_bytes():
        pass
    def read_until_close():
        pass
    def write():
        pass
    def close():
        pass

class FileIOStream(BaseIOStream):
    def __init__(self):
        pass
    def read_until_regex(self , regex , callback = None , max_bytes  = None):
        self._read_regex = re.compile(regex)
        self._read_max_bytes = max_bytes
        try:
            self._try_read_inline()
        except Exception as e:
            return
    def _set_read_callback(self , callback):
        if callback is not None:
            self._read_callback = stack.context.
class LocalFileWrapper(io.TextIOWrapper):

    def __init__(self , stream_object , *args , **kwargs):
        self.stream_object = stream_object
        try:
            super(FileIOStream , self).__init__(stream_object , *args , **kwargs)
        except Exception:
            pass

    def pipe_reader():


