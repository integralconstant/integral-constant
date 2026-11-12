class tree_node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        
root_node = tree_node()
root_node.data = "커피"

node1 = tree_node()
node1.data = "녹차"
root_node.left = node1

node2 = tree_node()
node2.data = "꿀물"
root_node.right = node2

node3 = tree_node()
node3.data = "아이스티"
node1.left = node3

node4 = tree_node()
node4.data = "레몬에이드"
node1.right = node4

node5 = tree_node()
node5.data = "카페모카"
node2.left = node5

print(root_node.data, end=" ")
print()
print(root_node.left.data, root_node.right.data, end=" ")
print()
print(root_node.left.left.data, root_node.left.right.data,
      root_node.right.left.data, end=" ")