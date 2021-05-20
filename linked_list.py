class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        #to keep track of head & tail/last_node
        #last_node/tail will always point to None
        
    def to_list(self):
        l = []
        if self.head is None:
            return l
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self):
        #will print starting from head, all way to tail
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self,data):
        #will add data to head
        if self.head is None:
            #first element will be both head & tail
            self.head = Node(data, None)
            self.last_node = self.head
            return
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self,data):
        #will add data to tail
        if self.head is None:
            #i.e. list is empty
            self.insert_beginning(data)
            return
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
        
        

ll = LinkedList()
ll.insert_beginning("data1")
# ll.insert_beginning("data2")
# ll.insert_beginning("data3")
ll.insert_at_end("data0")
ll.insert_at_end("data-1")
ll.print_ll()
print(ll.to_list())