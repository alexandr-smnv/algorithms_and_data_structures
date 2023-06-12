def selection_sort(array):
    for i in range(len(array)-1):
        idx_min = i     # индекс элемента с минимальным значением в "неотсортированном" списке

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:       # если итерируемый элемент меньше
                idx_min = j
        # Помещаем в конец "отсортированного" списка
        array[idx_min], array[i] = array[i], array[idx_min]

    return array
