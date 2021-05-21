class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size
        #fixed length list

    def custom_hash(self, key):
    # it converts key into index in our hashtable list,
    # this way we can obtain value for key in constant time,
        # bcoz accessing an index within a list takes O(1) or constant time
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            #adding int representation of unicode char
            #eg if i = "A" ord(i) returns 65 -> ASCII value
            #but many key can result in same value with this
            hash_value = (hash_value * ord(i)) % self.table_size #to add randomness
            #and remainder gives hash value which will never exceed table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            #i.e. this key is not used in table
            self.hash_table[hashed_key] = Node(Data(key, value), None)
            #The idea here isto reduce the possibility of having collisions 
            #most of the time we will be adding values to index that contains None
            #so inserting & retrieving will be O(1), if we implement better algo to
            #calculate hash_value chances of collision will be less.
        else:
            node  = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node  = self.hash_table[hashed_key]
            if node.next_node is None: #first node in linked list
                return node.data.value
            while node.next_node:
                if key == node.data.key: #other nodes
                    return node.data.value
                node = node.next_node
            if key == node.data.key: #final nodeinked list
                return node.data.value
        return None

    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node  = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None "
                    )
                    print(f" [{i}] {llist_string}")
                else:
                    print(f" [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f" [{i}] {val}")
        print("}")

# ht = HashTable(4)
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("ki", "Ram")
# ht.add_key_value("dog", "there")
# ht.print_table()