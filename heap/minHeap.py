class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        # bubble up（小さい方を上へ）
        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        size = len(self.heap)

        while True:
            min_index = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self.heap[left] < self.heap[min_index]:
                min_index = left

            if right < size and self.heap[right] < self.heap[min_index]:
                min_index = right

            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                break

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value
