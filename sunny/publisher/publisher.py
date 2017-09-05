from abc import ABCMeta,abstractmethod,abstractproperty
from six import with_metaclass
from pathlib import Path
from sh import tail
"""
This is the base publisher for the different type of subscriber
"""
class BasePubliser(with_metaclass(ABCMeta , object)):
    def __init__(self):
        self.TYPE_OF_PUBLISHER = None
        self.publisher = None

    @abstractmethod
    def get_publisher(self):
        """
        This is to get the raw publisher object
        """
        raise NotImplementedError()
    @abstractmethod
    def set_publisher(self,publisher_object = None):
        """
        This is to set the raw publisher object
        """
        raise NotImplementedError()

    publisher = property(get_publisher , set_publisher)

class FileNameNotRight(Exception):
    """
    Raise the exception when the file name is not string
    """
    pass

class FileNotFound(Exception):
    """
    Raise the exception when the file is not present at current location
    """
    pass

class FilePublisher(BasePubliser):
    """
    An implementation to get the data from the File
    """
    def __init__(self , columns =  None):
        self.TYPE_OF_PUBLISHER = "CSV_FILE"
        self.file_name = None
        self.columns = columns

    def set_publisher(self , file_name  = None):
        if type(file_name) is not str:
            raise FileNameNotRight("File name must be of string type.Check file_name")

        self.file_name = Path(file_name)
        if not self.file_name.exists() or not self.file_name.is_file():
            raise FileNotFound(self.file_name + "is not present")

    def get_publisher(self):
        return self.file_name





