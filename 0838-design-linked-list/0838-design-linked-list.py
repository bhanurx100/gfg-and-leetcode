class MyLinkedList:

    def __init__(self):
        self.arr = []

    def get(self, index: int) -> int:
        # O(1)
        return self.arr[index] if index < len(self.arr) and index >= 0 else -1

    def addAtHead(self, val: int) -> None:
        # O(n)
        self.arr.insert(0, val)

    def addAtTail(self, val: int) -> None:
        # O(1)
        self.arr.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        # O(n)
        if index == len(self.arr):
            self.addAtTail(val)
        elif index < len(self.arr) and index >= 0:
            self.arr.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.arr) and index >= 0:
            self.arr.pop(index)