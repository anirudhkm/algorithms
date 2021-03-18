import numpy as np


class Searching(object):
    """
    Searching algorithms
    """

    def __init__(self):

        pass

    @staticmethod
    def linear_search(lst, key):
        """
        Linear search algorithm.
        """

        i = 0
        while i < len(lst):
            if key == lst[i]:
                return i
            i+=1
        return -1

    @staticmethod
    def binary_search_iter(lst, key):
        """
        Binary search iter.
        """

        l = 0
        r = len(lst)-1
        while l <= r:
            
    def binary_search(self, lst, key, method="recursive"):
        """
        Binary search method.
        """

        if method == "iterative":
            binary_search_iter(lst, key)


    

a = Searching()
b = a.linear_search([23, 42, 12, 45, 12, 56, 99], 67)
print(b)