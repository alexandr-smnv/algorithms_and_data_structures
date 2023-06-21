def quick_sort(array):
    # базовый случай
    if len(array) < 2:
        return array
    else:
        # разделение
        pivot = array[-1]
        less = [i for i in array if i < pivot]
        center = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]
        
        # рекурсивный вызов и объединение
        return quick_sort(less) + center + quick_sort(greater)