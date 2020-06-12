"""
Define a buffer with a fixed size, so that when it fills up, adding another element must overide the oldest one.
"""
"""
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        append an element at the end of the buffer
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ =
    def get(self):
        pass

"""


class RingBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    class __Full:
        """ class that implements a full buffer """
        def append(self, item):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.capacity
        def get(self):
            """ return list of elements in correct order """
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self, item):
        """append an element at the end of the buffer"""
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data

