class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.End = Node(-1) #구현의 편의를 위해 dummy data를 넣어논거라고 함
        self.head = self.End    #더미 데이터를 왜 넣지??
        self.tail = self.End


    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None


    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)   #리스트가 비어 있으면 맨 앞에 원소를 넣어주는 것과 같은 로직

        else:   #사실상 들어온 node가 tail이 맞는데 -1 node를 그냥 tail로 둬서 계속 그 앞에 넣는거
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node


    def erase(self, node):
        next_node = node.next   #얘는 뭐지

        if node == self.head:
            node.next.prev = None   #temp = self.head 로 헤드를 임시로 저장해야하나?
            self.head = node.next
            node.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return next_node    # 얘를 왜 반환하는거지?


    def insert(self, node, new_data):
        if node == self.head:
            self.push_front(new_data)

        elif node == self.tail:
            self.push_back(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node


    def begin(self):
        return self.head


    def end(self):
        return self.tail


l = DoubleLinkedList()
l.push_back('a')
l.push_back('b')
l.push_back('c')

it = l.begin()  #Head니까 'a'를 가진 Node

print(it.data)  # 'a'
it = it.next
print(it.data)  # 'b'
it = it.prev
print(it.data)  # 'a'

it = l.erase(it)    # 해당 iterator의 Node를 삭제하고 그 다음 next.it 를 반환
print(it.data)  # 'b'

l.insert(it, 'd')   # 현재 iterator = 'b'의 노드, 그 앞에 'd'의 노드를 추가

it = l.begin()
while it != l.end():
    print(it.data , end = ' ')
    it = it.next

