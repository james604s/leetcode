class MyStack:

    def __init__(self):
        self.items = []
        
    def push(self, x: int) -> None:
        self.items.append(x)
        print("pushsi",self.items)

    def pop(self) -> int:
        element = self.items[-1]
        print("pope",element)
        self.items.pop(-1)
        print("popsi",self.items)
        return element

    def top(self) -> int:
        return self.items[-1]
        

    def empty(self) -> bool:
        return len(self.items) == 0