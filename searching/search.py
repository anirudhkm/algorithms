

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


def binary_search_iter(lst, key):
    """
    Binary search iter.
    """

    l, r = 0, len(lst)-1
    while l <= r:
        m = (l+r)//2
        if key < lst[m]:
            r = m-1
        elif key > lst[m]:
            l = m+1
        else:
            retun m
    return -1

def binary_search_recursive(lst, key, l, r):
    """
    Binary search in recursive style.
    """

    if l > r:
        return -1
    m = (l+r)//2
    if key > lst[m]:
        return binary_search_recursive(lst, key, m+1, r)
    elif key < lst[m]:
        return binary_search_recursive(lst, key, l, m-1)
    else:
        return m

def binary_search(self, lst, key, method="recursive"):
    """
    Binary search method.
    """

    if method == "iterative":
        binary_search_iter(lst, key)
    else:
        binary_search_recursive(lst, key)