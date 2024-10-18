import timeit
import random

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Timsort використовує вбудовану функцію sorted()
def timsort(arr):
    return sorted(arr)

# Функція для запуску тестів
def run_sorting_test(size):
    arr = [random.randint(0, size) for _ in range(size)]
    
    # Копії для різних алгоритмів
    arr_merge = arr[:]
    arr_insertion = arr[:]
    arr_timsort = arr[:]
    
    # Замір часу для Merge Sort
    merge_time = timeit.timeit(lambda: merge_sort(arr_merge), number=1)
    
    # Замір часу для Insertion Sort
    insertion_time = timeit.timeit(lambda: insertion_sort(arr_insertion), number=1)
    
    # Замір часу для Timsort
    timsort_time = timeit.timeit(lambda: timsort(arr_timsort), number=1)
    
    return merge_time, insertion_time, timsort_time

# Тестування на масивах різного розміру
sizes = [100, 1000, 5000, 10000, 20000]
for size in sizes:
    merge_time, insertion_time, timsort_time = run_sorting_test(size)
    print(f"Розмір масиву: {size}")
    print(f"Merge Sort: {merge_time:.5f} секунд")
    print(f"Insertion Sort: {insertion_time:.5f} секунд")
    print(f"Timsort: {timsort_time:.5f} секунд\n")

# Висновок:
# - Merge Sort стабільний та швидкий для великих масивів, але може поступатися Timsort, 
# який адаптований для реальних даних і поєднує переваги сортування вставками на маленьких частинах масиву.
# - Insertion Sort швидкий для дуже малих масивів, але непридатний для великих обсягів даних.
# - Timsort — найефективніший алгоритм, що використовується у Python, саме завдяки своєму гібридному підходу.