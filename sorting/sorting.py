

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


def merge(lst, l, m, r):
    """
    Perform merging on the list.
    """
    
    temp = [0]*len(lst)
    i, j, k = l, m+1, l
    while i <= m and j <= r:
        if lst[i] <= lst[j]:
            temp[k] = lst[i]
            i+=1
        else:
            temp[k] = lst[j]
            j+=1
        k+=1
    while i <= m:
        temp[k] = lst[i]
        k+=1
        i+=1
    while j <= r:
        temp[k] = lst[j]
        k+=1
        j+=1
    for i in range(l, r+1):
        lst[i] = temp[i]

def merge_sort(lst, l, r):
    """
    Merge sort implementation.
    """
    
    if l < r:
        m = (l+r)//2
        merge_sort(lst, l, m)
        merge_sort(lst, m+1, r)
        merge(lst, l, m, r)