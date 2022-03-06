class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val-self.min_value)
            self.min_value = val if self.min_value > val else self.min_value 
        else:
            self.stack.append(0)
            self.min_value=val

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                self.min_value = self.min_value - diff

    def top(self) -> int:
        if self.stack:
            diff = self.stack[-1]
            if diff < 0:
                return self.min_value
            else:
                return self.min_value + diff

    def getMin(self) -> int:
        if self.stack:
            return self.min_value
