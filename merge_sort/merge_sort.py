def merge_two_list(a, b):
    c = []      # результирующий список
    i = j = 0       # указатели
    while i < len(a) and j < len(b):        # пока указатели меньше длин списков
        # сравниваем элементы двух списков на которые указывают i и j
        # меньший добавляем в результирующий список
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # добавляем остальные значения, которые остались в большем по длине списке
    if i < len(a):
        c = c + a[i:]
    if j < len(b):
        c = c + b[j:]
    return c


def merge_sort(arr):
    if len(arr) > 1:
        # рекурсивно делим список пополам пока длина списка не будет равно 1
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge_two_list(left, right)      # слияние двух отсортированных списков
    else:
        return arr
