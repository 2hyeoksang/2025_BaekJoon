class Stack:
    def __init__(self):
        self.arr = []

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.arr == []:
            return -1

        return self.arr.pop(-1)

    def size(self):
        return len(self.arr)

    def is_empty(self):
        if self.arr == []:
            return 1

        return 0

    def top(self):
        if self.arr == []:
            return -1

        return self.arr[-1]


n = int(input())
stack = Stack()

for _ in range(n):
    order = input()
    if 'push' in order:
        order1, num = list(order.split())
        num = int(num)
        stack.push(num)

    elif order == 'pop':
        print(stack.pop())

    elif order == 'size':
        print(stack.size())

    elif order == 'empty':
        print(stack.is_empty())

    elif order == 'top':
        print(stack.top())