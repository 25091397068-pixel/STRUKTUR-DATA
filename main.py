"""
ADT ARRAY - As defined in the document
One-dimensional array, fixed size, accessed via index
"""

class Array:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size  # inisialisasi array dengan 0

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index di luar batas")

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index di luar batas")
        self._data = [None] * size
    
    def length(self):
        """length(): Mengembalikan panjang array"""
        return self._size
    
    def getitem(self, index):
        """getitem(index): Mengambil nilai di indeks tertentu"""
        if index < 0 or index >= self._size:
            raise IndexError("Indeks di luar jangkauan")
        return self._data[index]
    
    def setitem(self, index, value):
        """setitem(index, value): Mengubah nilai di indeks tertentu"""
        if index < 0 or index >= self._size:
            raise IndexError("Indeks di luar jangkauan")
        self._data[index] = value
    
    def clearing(self, value):
        """clearing(value): Mengosongkan array dengan nilai tertentu"""
        for i in range(self._size):
            self._data[i] = value
    
    def __iter__(self):
        """iterator(): Membuat iterator untuk traversal"""
        return ArrayIterator(self._data)

    def get_size(self):
        return self.size

    def display(self):
        return self.data
class ArrayIterator:
    """Iterator untuk menelusuri array"""
    def __init__(self, data):
        self._data = data
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._data):
            value = self._data[self._index]
            self._index += 1
            return value
        raise StopIteration
