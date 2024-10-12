import timeit
import random

# Генеруємо випадкові дані для тестування
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Вбудоване сортування Timsort
def timsort(arr):
    return sorted(arr)

# Розмір масиву для тестування
data_size = 10000

# Генерація даних
data = generate_data(data_size)

# Порівняння часу виконання кожного алгоритму
insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
timsort_time = timeit.timeit(lambda: timsort(data.copy()), number=1)

# Виведення результатів
print(f"Сортування вставками: {insertion_time:.5f} секунд")
print(f"Сортування злиттям: {merge_time:.5f} секунд")
print(f"Timsort (вбудоване сортування): {timsort_time:.5f} секунд")


