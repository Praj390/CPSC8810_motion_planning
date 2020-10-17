# utils.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to Clemson University and the authors.
# 
# Author: Ioannis Karamouzas (ioannis@g.clemson.edu)


class Value():
    """A helper class for adding f & g values to your PriorityQueue """

    def __init__(self, f, g):
        self.g = g
        self.f = f

class OrderedSet:
    """ An ordered list of elements """
    
    def __init__(self):
        self._container = []
    
    def add(self, item):
        if item in self._container:
            self._container.append(item)
        else:
            self._container.append(item)

    def has(self, item):
        return self._container.__contains__

    def remove(self, item):
        if item in self._container:
            self._container.remove(item)
    
    def clear(self):
        self._container.clear()
    
    def __contains__(self, item):
        return self._container.__contains__(item)

    def __len__(self):
        return self._container.__len__()
    
    def __iter__(self):
        return self._container.__iter__()
    
    def pop(self, last=True):
        if last:
            e = self._container.pop()
        else:
            e = self._container.pop(0)
        return e

class PriorityQueue:
    """
        A Queue in which the minimum (or maximum) element (as determined by f and
        order) is returned first.
    """
    def __init__(self, order=min, f=lambda v:v):
        if order == min or order == "min":
            self.order = min
        elif order == max or order == "max":
            self.order = max
        else:
            raise KeyError("order must be min or max")
        self.f = f

        self._dict = {}
  
    def get(self, item):
        return self._dict.__getitem__(item)

    def put(self, item, value):
        if item not in self._dict:
            self._dict[item] = value
        else:
            self._dict[item] = value

    def has(self, item):
        return self._dict.__contains__(item)

    def remove(self, item):
        if item in self._dict:
            del self._dict[item]

    def pop(self):
        if len(self._dict) > 0:
            tar = self.order(self._dict, key=lambda k: self.f(self._dict.get(k)))
            val = self._dict[tar]
            del self._dict[tar]
            return tar, val
        raise IndexError("pop from empty priority queue")

    def __iter__(self):
        return self._dict.__iter__()
    
    def __contains__(self, item):
        return self._dict.__contains__(item)

    def __len__(self):
        return self._dict.__len__()

    def __getitem__(self, key):
        return self._dict.__getitem__(key)
    
    def __setitem__(self, key, value):
        return self._dict.__setitem__(key, value)
    
    def __delitem__(self, key):
        return self._dict.__delitem__(key)