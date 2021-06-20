import ctypes

class XorList:
    def __init__(self, val, curr=None):
        self.val = val
        prev = curr - 1 if curr > 0 else 0
        _next = curr + 1
        self.both = prev ^ _next

    def __getitem__(self, ind):

