from abc import ABCMeta,abstractmethod,abstractproperty
from six import with_metaclass

class BaseFilter(with_metaclass(object , ABCMeta)):
    """
    Base class for any kind of filter information
    """
    @abstractmethod
    def get_filter(self):
        raise NotImplementedError()

    @abstractmethod
    def set_filter(self):
        raise NotImplementedError()

    @abstractmethod
    def reset_filters(self):
        raise NotImplementedError()

    @abstractmethod
    def add_filter(self):
        raise NotImplementedError()

