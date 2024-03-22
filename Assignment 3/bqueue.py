class ChemicalQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_full(self):
        return len(self.queue) >= self.size

    def enqueue(self, chemical):
        if not self.is_full():
            self.queue.append(chemical)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def __repr__(self):
        return f"{self.queue}"