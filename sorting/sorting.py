

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