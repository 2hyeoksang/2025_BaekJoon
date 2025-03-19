class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0


    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None    # 이거 왜 있누

        else:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None    # 얘도 왜 있음?

        self.node_num += 1


    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None:
            self.tail = new_node
            self.head = new_node
            new_node.next = None

        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

        self.node_num += 1


    def pop_front(self):
        if self.head == None:
            print('List is empty.')

        elif self.head.next == None:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num -= 1

            return temp.data

        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None    #self.head.next에 앞의 data Node가 담겨있으므로 끊어주기
            self.node_num -= 1

            return temp.data


    def pop_back(self):
        if self.tail == None:
            print("List is empty.")

        elif self.tail.prev == None:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num -= 1

            return temp.data

        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1

            return temp.data


    def size(self):
        return self.node_num


    def empty(self):
        return self.node_num == 0


    def front(self):
        if self.head == None:
            print('List is empty')

        else:
            return self.head.data


    def back(self):
        if self.tail == None:
            print("List is empty.")

        else:
            return self.tail.data

    def __str__(self):
        if self.head == None:
            return 'List is empty'

        else:
            curr = self.head
            print(curr.data)

            while curr.next != None:
                curr = curr.next
                print(curr.data)

            return 'end'


l = DoubleLinkedList()
l.push_front(3)
l.push_front(5)
l.push_back(9)
l.push_back(-10)
print(l)