class MinHeap:
    def __init__(self, cap=10):
        self.heap_size = 0 #current number of elements in the heap 
        self.capacity = cap #max number of elements heap can store 
        self.array = [0] * cap #initialize array of capacity 
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2
    def get_min(self):
        return self.array[0]
    def swap(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]
    def heapify_up(self,i):
        while i>0 and self.array[i]< self.array[self.parent(i)]:
            self.swap(i,self.parent(i))
            i=self.parent(i)

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
        smallest = i
        if l < self.heap_size and self.array[l] < self.array[i]:
            smallest = l
        if r < self.heap_size and self.array[r] < self.array[smallest]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)

    def extract_min(self):
        if self.heap_size <= 0:
            print ('empty tree')
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.array[0]

        root = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify_down(0)

        return root

    def decrease_key(self, i, new_val):
        self.array[i] = new_val
        self.heapify_up(i)

    def delete_key(self, i):
        self.decrease_key(i, float('-inf'))
        return self.extract_min()

    def print_heap(self):
        print("Min Heap:")
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
        if self.heap_size == 0:
            return None
        return self.array[0]
if __name__ == "__main__":
    h = MinHeap(11)
    h.insert_key(3)
    h.insert_key(2)
    h.insert_key(15)
    h.insert_key(5)
    h.insert_key(4)
    h.insert_key(45)
    h.print_heap()
    print()
    print("Extracting Data From Min Heap")
    while h.heap_size > 0:
        print(h.extract_min(), end=' ')
    print()
    h.insert_key(3)
    h.insert_key(2)
    h.insert_key(15)
    h.insert_key(5)
    h.insert_key(4)
    h.insert_key(45)
    h.print_heap()
    print("Extract Min:", h.extract_min())
    print("Get Min:", h.get_min())
    h.delete_key(0)
    h.print_heap()
    print("Get Min After Deleting 0:", h.get_min())
    h.decrease_key(4, 1)
    print("Get Min After Decreasing the Key at index 4 to 1:", h.get_min())
    print("Extracting Data Again From Min Heap")
    while h.heap_size > 0:
        print(h.extract_min(), end=' ')
    print()

            
