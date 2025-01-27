import heapq

# Heapsort Implementation
def heapsort(arr):
    n = len(arr)
    build_max_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        max_heapify(arr, 0, i)
    return arr

def build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)

def max_heapify(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)