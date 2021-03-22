

def selection_sort(lst):
    """
    Selection sort implementation
    """

    l = len(lst)
    for i in range(l-1):
        pos = i
        for j in range(i+1, l-1):
            if lst[j] < lst[pos]:
                pos = j
        temp = lst[pos]
        lst[pos] = lst[i]
        lst[i] = temp
    return lst


def insertion_sort(lst):
    """
    Perform insertion sort.
    """
    
    for i in range(1, len(lst)):
        pos = i
        val = lst[i]
        while pos > 0 and lst[pos-1] > val:
            lst[pos] = lst[pos-1]
            pos = pos - 1
        lst[pos] = val
    return lst

