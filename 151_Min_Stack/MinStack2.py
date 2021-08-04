class MinStack:

    def __init__(self):
        """
        initialize your data structure here.

        空間換取時間
        """
        self.stack = []
        self.min_states = []

    def push(self, x):
        self.stack.append(x)
        self.min_states.append(min(x, self.min_states[-1]) if self.min_states else x)

    def pop(self):
        self.stack.pop()
        self.min_states.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_states[-1]