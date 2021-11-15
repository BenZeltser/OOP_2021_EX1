
'''
    Code imported from www.newbedev.com
'''


class heap:

    def maxheapify(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self._maxheapify(array, n, i)

    def _maxheapify(self, array, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and array[l] > array[i]:
            largest = l
        else:
            largest = i
        if r < n and array[r] > array[largest]:
            largest = r
        if (largest != i):
            array[largest], array[i] = array[i], array[largest]
            self._maxheapify(array, n, largest)

    def minheapify(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self._minheapify(array, n, i)

    def _minheapify(self, array, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and array[l] < array[i]:
            smallest = l
        else:
            smallest = i
        if r < n and array[r] < array[smallest]:
            smallest = r
        if (smallest != i):
            array[smallest], array[i] = array[i], array[smallest]
            self._minheapify(array, n, smallest)

    def descending_heapsort(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self._minheapify(array, n, i)
        for i in range(n - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            self._minheapify(array, i, 0)

    def ascending_heapsort(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self._maxheapify(array, n, i)
        for i in range(n - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            self._maxheapify(array, i, 0)


b = [550, 4520, 3, 2340, 12]
a = heap()

a.maxheapify(b)
print('Max Heapify -->', b)

a.minheapify(b)
print('Min Heapify -->', b)

a.ascending_heapsort(b)
print('Ascending Heap Sort -->', b)

a.descending_heapsort(b)
print('Descending Heap Sort -->', b)