class Flask:
    CAPACITY = 4
    # Mapping of chemical names to their colors
    COLORS = {
        'AA': '\033[91m',
        'BB': '\033[34m',
        'CC': '\033[32m',
        'DD': '\033[33m',  
        'EE': '\033[33m',
        'FF': '\033[95m',
        'RESET':'\033[0m'
    }

    def __init__(self):
        self.stack = []

    def is_full(self):
        return len(self.stack) >= Flask.CAPACITY

    def add_chemical(self, chemical):
        if not self.is_full():
            self.stack.append(chemical)

    def remove_top_chemical(self):
        if self.stack:
            return self.stack.pop()
        return None

    def top_chemical(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_sealed(self):
        if len(self.stack) == 3 and len(set(self.stack)) == 1:
            return True
        return False

