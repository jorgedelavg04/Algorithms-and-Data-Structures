class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        n = self.start_node
        while n is not None:
            print(n.item, "")
            n = n.ref

    def insert_node_from_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_node_from_back(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_node_after_element(self, element, data):
        if self.start_node is None:
            print("List is empty")
            return
        n = self.start_node
        while n is not None:
            if element is n.item:
                break
            n = n.ref
        if n is None:
            print("Item was not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_node_before_element(self, element, data):
        if self.start_node is None:
            print("List is empty")
            return
        
        new_node = Node(data)

        if self.start_node.item is element:
            new_node.ref = self.start_node
            self.start_node = new_node

        n = self.start_node
        while n.ref is not None:
            if element is n.ref.item:
                break
            n = n.ref
        if n.ref is None:
            print("Item was never found") 
        else:
            new_node.ref = n.ref
            n.ref = new_node

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.insert_node_from_start(5)
    my_list.insert_node_from_start(2)
    my_list.insert_node_from_back(39)
    my_list.insert_node_after_element(2, 299929292992)
    my_list.insert_node_before_element(5, 10)
    my_list.traverse_list()