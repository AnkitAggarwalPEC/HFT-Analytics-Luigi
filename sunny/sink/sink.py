from abc import ABCMeta,abstractmethod,abstractproperty
from six import with_metaclass
class Sink(with_metaclass(ABCMeta ,object)):
    """
    A sink is abstraction for where data to be finally store for example a file or in a database.This is inspired from luigi target
    """
    @abstractmethod
    def exists(self):
        """
        Returns True if the sink exists and false otherwise
        """

class FileSystem(with_metaclass(ABCMeta , object)):
    """
    This is the abstraction used alongside with FileSystem Sink
    A FileSystem will be associated with FileSystemSink
    """
    def remove(self, path , recursive = True , skip_trash = True):
        """
        Remove a file or directory at path
        :recursive : If the path is directory, clean the whole directory if true
        """
        pass
        raise NotImplementedError("remove() not implemented on {0}".format(self.__class__.__name__))

    def mkdir(self, path , parents=True , raise_if_exists = True):
        """
        Create a directory at the particular location
        :param parents : Create parent directory when necessary
        :param raise_if_exists: Raise a exception if the file already exists
        """
        raise NotImplementedError("mkdir() not implemented on {0}".format(self.__class__.__name__))

    def isdir(self , path):
        """
        Return True if the location at the path is a directory and otherwise false
        """
        raise NotImplementedError("isDir() not implemented on {0}".format(self.__class__.__name__))

    def listdir(self , path):
        """
        Return the list of the files present at the path
        """
        raise NotImplementedError("listdir() not implemented on {0}".format(self.__class__.__name__))

    def move(self , path , dest):
        """
        Move a file from a path to the dest
        """
        raise NotImplementedError("move() not implemented on {0}".format(self.__class__.__name__))
    def rename(self , *args , **kwargs):
        """
        Rename the file
        """
        self.move(*args , **kwargs)

    def copy(self , src , dest):
        """
        Copy a file or directory to the given dest
        """
        raise NotImplementedError("copy() not implemented on {0}".format(self.__class__.__name__))


class FileSystemSink(Sink):
    """
    File sink a sink for the data file
    """
    def __init__(self  , path):
        """
        Initialize the path where to store the data
        """
        self.path = path

    @abstractproperty
    def fs(self):
        raise NotImplementedError()

    @abstractmethod
    def open(self, mode):
        """
        Open the filesystem sink
        :param "r" opening the file for read only mode and "w"  for write only mode
        """
        pass
    def exists(self):
        """
        Return True if the file exists at the path
        """
        return self.fs.exists(self.path)

    def remove(self):
        """
        Remove the file at the path
        """
        return self.fs.remove(self.path)


