class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        out_str = f"Node[{self.data}]"
        temp = self.next
        while temp is not None:
            out_str += f"Node[{temp.data}]"
            temp = temp.next

        return out_str
    
    def addNode(self, node):
        if self.next:
            temp = self.next
            node.next = temp
            self.next = node

        else:
            self.next = node


my_list = Node("alice")
print(my_list)
bob_node = Node("bob")
my_list.addNode(bob_node)
print(my_list)

amy_node = Node("amy")
carl_node = Node("carl")

my_list.next.addNode(carl_node)
my_list.addNode(amy_node)

print(my_list)

cam_node = Node("cam")
my_list.next.next.addNode(cam_node)
print(my_list)
