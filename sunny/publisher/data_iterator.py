from abc import ABCMeta,abstractmethod,abstractproperty
from six import with_metaclass
"""
This is used to iterate any kind of the iterables like(Socket, Files)
"""
class BaseIterator(with_metaclass(ABCMeta , object)):
    _undefined = object()
    def __init__(self, iterable , start = None , end = undefined , skip_delimter = True ):
        """
        This function is meant for the initailization purpose
        """
        pass
    @abstractmethod
    def __iter__(self):
        """
        This will return the iterable object
        """
        raise NotImplementedError("This is not implemented yet")

    @abstractmethod
    def next(self):
        """
        This will yeild the new line depending upon the type of iterator
        """
        raise NotImplementedError("This is not implemented yet")

class TailIterator(BaseIterator):
    def __init__(self , iterable , start = None , end =  BaseIterator._undefined , skip_delimter =  True ):
        """
        Here iterable will the file name
        """
        self.iterable = iterable
        self.start = start
        self.end = end
        self.skip_delimter = skip_delimter

    def __iter__(self):
        return self

    def next(self):
        """
        This will yield the next line based on the start and end_object
        """









