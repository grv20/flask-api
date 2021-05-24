class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return
            #that means value=node & binary search tree should not have duplicate values


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else: 
            self._insert_recursive(data, self.root)
            #we are using _ bcoz this method will only b used by insert function

    def _search_recursive(self, blog_post_id, node):
        if blog_post_id == node.data["id"]: #current node gives the data
            return node.data

        if blog_post_id < node.data["id"] and node.left is not None:
            #required data is less than current node data and
            #data less than current node do exist in tree
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            return self._search_recursive(blog_post_id, node.left)

        if blog_post_id > node.data["id"] and node.right is not None:
            #required data is greater than current node data and
            #data greater than current node do exist in tree
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            return self._search_recursive(blog_post_id, node.right)

        return False

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self._search_recursive(blog_post_id, self.root)


#the order in which we insert data into binary search tree matters.
#It will impact the performance of our tree.
#Number of data points corresponds to height of tree
#Your sub-tree heights should be as close as possilble to make it efficient.
#Eg root is 20, so left sub tree will have numbers less than 20, while right
#will have all numbers > 20, which makes it possible that height of both sub-trees
#will vary by big difference(depending on range)

#if we insert starting from lowets to highest, it will actually result in
#linkedList kind of structure, since all sub trees will be at right.
#And that will lead us to search time of O(n)
