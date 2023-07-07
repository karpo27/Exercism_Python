class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        if values is None:
            values = []
        self.first = None
        self.length = 0

        for value in values:
            self.push(value)

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node.value()
            node = node.next()

    def head(self):
        if self.length == 0:
            raise EmptyListException()
        return self.first

    def push(self, value):
        node = Node(value)
        node._next = self.first
        self.first = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise EmptyListException()
        node = self.first
        self.first = node.next()
        self.length -= 1

        return node.value()

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

        message: explanation of the error.

        """

    def __init__(self, message="The list is empty."):
        super().__init__(message)
