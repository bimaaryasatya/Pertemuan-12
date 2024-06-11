# queue.py
from dataclasses import dataclass
from typing import Any

@dataclass
class Standard_Queue:
    """Struktur data antrian sederhana"""
    max_size: int = None
    elements: list[Any] = None

    def __post_init__(self):
        if self.elements is None:
           self.elements = []
        if self.max_size is None:
            self.max_size = float('inf')
    
    def enqueue(self, element: Any) -> None:
        """Tambahkan elemen ke akhir antrian"""
        if self.isFull():
            raise IndexError("Cannot enqueue to a full queue")
        self.elements.append(element)

    def dequeue(self) -> Any:
        """Hapus dan kembalikan elemen depan antrian"""
        if self.isEmpty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.elements.pop(0)

    def isEmpty(self) -> bool:
        """Periksa apakah antrian kosong"""
        return not self.elements

    def isFull(self) -> bool:
        """Periksa apakah antrian penuh"""
        return len(self.elements) == self.max_size

    def cur_size(self) -> int:
        """Kembalikan jumlah elemen dalam antrian"""
        return len(self.elements)
    
    def setSize(self, i: int) -> Any:
        """Set ukuran antrian"""
        self.max_size = i
        return self
    
    def size(self) -> int:
        """Kembalikan ukuran antrian"""
        return self.max_size
    
    def first(self) -> Any:
        """Kembalikan elemen pertama antrian"""
        if self.isEmpty():
            raise IndexError("Cannot get first element from an empty queue")
        return self.elements[0]
    
    def last(self) -> Any:
        """Kembalikan elemen terakhir antrian"""
        if self.isEmpty():
            raise IndexError("Cannot get last element from an empty queue")
        return self.elements[-1]