

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

def bubble_sort(lst):
    """
    Bubble sort implementation...
    """
    
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def shell_sort(lst):
    """
    Shell sorting of list.
    """
    n = len(lst)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            j = i - gap
            gval = lst[i]
            while j >=0 and lst[j] > gval:
                lst[j+gap] = lst[j]
                j = j-gap
            lst[j+gap] = gval
        gap = gap//2
    return lst

