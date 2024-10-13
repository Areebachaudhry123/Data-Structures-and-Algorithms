class MaxHeap:
    def __init__(self, cap=10):
        self.heap_size = 0  # current number of elements in the heap
        self.capacity = cap  # max number of elements heap can store
        self.array = [0] * cap  # initialize array of capacity

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get_max(self):
        return self.array[0] if self.heap_size > 0 else None

    def swap(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def heapify_up(self, i):
        while i > 0 and self.array[i] > self.array[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def insert_key(self, k):
        if self.heap_size == self.capacity:
            print("\nOverflow: Could not insertKey")
            return
        self.heap_size += 1
        i = self.heap_size - 1
        self.array[i] = k
        self.heapify_up(i)

    def heapify_down(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.array[l] > self.array[i]:
            largest = l
        if r < self.heap_size and self.array[r] > self.array[largest]:
            largest = r
        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)

    def extract_max(self):
        if self.heap_size <= 0:
            print('Empty tree')
            return None

        root = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify_down(0)

        return root

    def increase_key(self, i, new_val):
        self.array[i] = new_val
        self.heapify_up(i)

    def delete_key(self, i):
        if i < 0 or i >= self.heap_size:
            print("Index out of range")
            return None

        self.increase_key(i, float("inf"))
        return self.extract_max()

    def print_heap(self):
        print("Max Heap:", end=" ")
        for i in range(self.heap_size):
            print(self.array[i], end=" ")
        print()

    def is_empty(self):
        return self.heap_size == 0

    def is_full(self):
        return self.heap_size == self.capacity

    def search(self, key):
        for i in range(self.heap_size):
            if self.array[i] == key:
                return i
        return -1

    def peek(self):
        return self.array[0] if self.heap_size > 0 else None


if __name__ == "__main__":
    h = MaxHeap(11)
    h.insert_key(3)
    h.insert_key(2)
    h.insert_key(15)
    h.insert_key(5)
    h.insert_key(4)
    h.insert_key(45)
    h.print_heap()

    print("\nExtracting Data From Max Heap")
    while h.heap_size > 0:
        print(h.extract_max(), end=' ')
    print()

    h.insert_key(3)
    h.insert_key(2)
    h.insert_key(15)
    h.insert_key(5)
    h.insert_key(4)
    h.insert_key(45)
    h.print_heap()

    print("Extract Max:", h.extract_max())
    print("Get Max:", h.get_max())

    h.delete_key(0)
    h.print_heap()
    print("Get Max After Deleting 0:", h.get_max())

    h.increase_key(4, 50)
    print("Get Max After Increasing the Key at index 4 to 50:", h.get_max())

    print("Extracting Data Again From Max Heap")
    while h.heap_size > 0:
        print(h.extract_max(), end=' ')
    print()
