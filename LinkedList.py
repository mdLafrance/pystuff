import sys
import re

__all__ = ["LinkedListNode", "LinkedList"]

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, iterable=None):
        self.first = None
        self.last = None

        self.iterItem = None # For iterable implementation
        self.firstIter = True

        if iterable is not None:
            try:
                for item in iterable:
                    self.add(item)
            except TypeError:
                print("Error, could not build linkedlist out of non-iterable item")

    def __add__(self, o):
        self.last.next = o.first
        
    def __str__(self):
        s = ""

        ptr = self.first

        while ptr is not None:
            s += "{} -> ".format(str(ptr))

            ptr = ptr.next

        s += "NULL"

        return s

    def __len__(self):
        ptr = self.first

        length = 0

        while ptr is not None:
            length += 1
            ptr = ptr.next

        return length

    def __getitem__(self, i):
        if i < 0:
            raise IndexError("Negative index supplied")
        
        if i > len(self)-1:
            raise IndexError("Index greater than size of LinkedList")

        ptr = self.first

        k = 0

        while k < i:
            ptr = ptr.next

            k += 1

        return ptr

    def __iter__(self):
        self.iterItem = self.first
        self.firstIter = True

        return self

    def __next__(self):
        if not self.firstIter:
            self.iterItem = self.iterItem.next
        else:
            self.firstIter = False

        if self.iterItem is None:
            raise StopIteration()

        return self.iterItem

    def add(self, node):
        if not isinstance(node, LinkedListNode):
            llnode = LinkedListNode(node)

        if self.first is None:
            self.first = llnode

        if self.last is not None:
            self.last.next = llnode

        self.last = llnode

    def reverse(self):
        last = self.last

    def intersection(self, o):
        selfItems = set()
        
        for i in self:
            selfItems.add(i.val)

        for i in o:
            if i.val in selfItems:
                return i.val

        return None

if __name__ == "__main__":
    a = LinkedList([1,2,3,4])
    b = LinkedList([6,3,4])

    print(a.intersection(b))