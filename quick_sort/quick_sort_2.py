def quick_sort(L, left=0, right=None):
    if right is None:
        right = len(L)

    if right - left > 1:
        # Разделяй
        mid = partition(L, left, right)

        # Властвуй
        quick_sort(L, left, mid)
        quick_sort(L, mid + 1, right)


def partition(L, left, right):
    pivot = right - 1
    i = left    # Индекс в левой половине
    j = pivot - 1   # Индекс в правой половине

    while i < j:
        # Перемещение i в позицию элемента >= L[pivot]
        while L[i] < L[pivot]:
            i = i + 1

        # Перемещение j в позицию элемента < L[pivot]
        while i < j and L[j] >= L[pivot]:
            j = j - 1

        # Обмен местами элементов i и j, если i < j
        if i < j:
            L[i], L[j] = L[j], L[i]

    # Размещение центрального элемента в надлежащем месте.
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i

    # Возврат индекса центрального элемента.
    return pivot