# Author: Jun Kim
# Description: In this program we will implement a MinHeap class.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        adds a new object to the MinHeap maintaining heap property
        """
        if self.is_empty():
            self.heap.append(node)
            return

        self.heap.append(node)
        index = self.heap.length()-1


        parent_index = (index - 1) // 2
        parent_node = self.heap.get_at_index(parent_index)

        i = index

        while i < self.heap.length():

            if self.heap.get_at_index(index) < self.heap.get_at_index(parent_index):

                self.heap.swap(index, parent_index)

                index = parent_index
                parent_index = (index - 1) // 2


                if index == 0:
                    return

                i = parent_index

            else:
                return





    def parent(self,index):
        """
        returns index of parent node
        """
        
        return (index - 1) // 2

    def left(self,index):
        """
        returns index of left node
        """
        return 1 + index*2

    def right(self,index):
        """
        returns index of right node
        """
        return 2 + index*2

    def get_min(self) -> object:
        """
        returns an object with a minimum key without removing it from the heap
        """

        if self.is_empty():
            raise MinHeapException()

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        returns an object with a minimum key and removes it from the heap
        """

        if self.is_empty():
            raise MinHeapException()

        val = self.heap.get_at_index(0)
        lastval = self.heap.pop()

        if self.is_empty():
            return val

        self.heap.set_at_index(0,lastval)

        self.percolate_down(0)


        return val

    def percolate_down(self, i):


        while i < self.heap.length():

            index = i

            left_index = 1 + index * 2
            right_index = 2 + index * 2

            if self.heap.length() == 2:
                if self.heap.get_at_index(0) < self.heap.get_at_index(1):
                    return
                else:
                    self.heap.swap(0,1)
                    return

            if left_index > self.heap.length()-1:
                return

            if right_index > self.heap.length()-1:
                return


            small = None

            value = self.heap.get_at_index(index)

            left = self.heap.get_at_index(left_index)
            right = self.heap.get_at_index(right_index)


            if left_index < self.heap.length() and value > left:
                small = left_index
                value = left

            if right_index < self.heap.length() and value > right:
                small = right_index
                value = right

            if small != None:

                self.heap.swap(i,small)
                temp = i
                i = small
                small = temp


            else:
                break

    def build_heap(self, da: DynamicArray) -> None:
        """
        receives a dynamic array with objects in any order and builds a proper
        MinHeap from them
        """

        while self.heap.length() != 0:

            self.heap.pop()


        for i in range(da.length()):
            self.add(da.get_at_index(i))


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
