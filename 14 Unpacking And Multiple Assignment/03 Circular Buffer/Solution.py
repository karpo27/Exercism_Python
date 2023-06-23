class BufferFullException(BufferError):
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = capacity
        self.buffer = []

    def read(self):
        if self.slots < self.capacity:
            item = self.buffer[0]
            self.buffer.pop(0)
            self.slots += 1
            return item
        else:
            raise BufferEmptyException("Circular buffer is empty")

    def write(self, data):
        if self.slots > 0:
            self.buffer.append(data)
            self.slots -= 1
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if self.slots == self.capacity:
            raise BufferEmptyException("Circular buffer is empty")
        elif 0 < self.slots < self.capacity:
            self.write(data)
        else:
            self.buffer.pop(0)
            self.buffer.append(data)

    def clear(self):
        self.buffer.clear()
        self.slots = self.capacity
