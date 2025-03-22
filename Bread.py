class Bread:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.END = Bread(-1)
        self.head = self.END
        self.tail = self.END


    def push_back(self, new_data):
        new_Bread = Bread(new_data)

        if self.head == self.tail:
            new_Bread.next = self.head
            self.head.prev = new_Bread
            self.head = new_Bread

        else:
            new_Bread.prev = self.tail.prev
            self.tail.prev.next = new_Bread
            new_Bread.next = self.tail
            self.tail.prev = new_Bread


    def insert(self, node, new_data):
        new_bread = Bread(new_data)

        if node == self.head:
            temp = self.head
            temp.prev = new_bread
            new_bread.next = temp
            self.head = new_bread

        elif node == self.tail:
            self.tail.prev.next = new_bread
            new_bread.prev = self.tail.prev
            new_bread.next = self.tail
            self.tail.prev = new_bread

        else:
            node.prev.next = new_bread
            new_bread.prev = node.prev
            new_bread.next = node
            node.prev = new_bread


    def erase(self, node):
        next_node = node.next

        if node == self.head:
            node.next.prev = None
            self.head = node.next
            node.next = None

        elif node == self.tail:
            next_node = node
            pass

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev =  None
            node.next = None

        return next_node


    def end(self):
        return self.tail


    def __str__(self):
        curr = self.head
        while curr != self.tail:
            print(curr.data, end = '')
            curr = curr.next
        return ''



n, m = tuple(map(int,input().split()))
recipe = list(input())
l = DLL()
for ele in recipe:
    l.push_back(ele)

it = l.end()
for _ in range(m):
    order = input().split()
    cmd = order[0]
    if cmd == 'L':
        if it.prev is None:
            pass
        else:
            it = it.prev

    elif cmd == 'R':
        if it.next is None:
            pass
        else:
            it = it.next

    elif cmd == "D":
        it = l.erase(it)

    elif cmd == "P":
        data = order[1]
        l.insert(it, data)

print(l)
