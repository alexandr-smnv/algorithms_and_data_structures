def insertion_sort(list):
    for i in range(1, len(list)):
        j = i -1        # индекс текущего элемента
        element_next = list[i]      # следующий элемент
        while (list[j] > element_next) and (j >= 0):        # пока текущий элемент больше следующего и индекс текущего больше либо равен нулю
            list[j+1] = list[j]     # меняем местами число, продвигая по списку
            j = j - 1
        list[j+1] = element_next    # вставляем элемент на нужное место
    return list
