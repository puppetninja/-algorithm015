class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque_list = []
        self.deque_size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque_list) < self.deque_size:
            self.deque_list = [value] + self.deque_list
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque_list) < self.deque_size:
            self.deque_list = self.deque_list + [value]
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque_list) > 0:
            self.deque_list = self.deque_list[1:]
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque_list) > 0:
            self.deque_list = self.deque_list[:-1]
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.deque_list) > 0:
            return self.deque_list[0]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.deque_list) > 0:
            return self.deque_list[-1]
        else:
            return  -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.deque_list) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque_list) == self.deque_size
