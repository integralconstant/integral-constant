class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
#첫 번째 노드 생성 - 링크 필요 X        
node1 = Node()
node1.data = "다현0"

#두 번째 노드 생성 - 첫 번째 노드와 연결
node2 = Node()
node2.data = "다현1"
node1.link = node2

node3 = Node()
node3.data = "다현2"
node2.link = node3

node4 = Node()
node4.data = "다현3"
node3.link = node4

node5 = Node()
node5.data = "다현4"
node4.link = node5

print(node1.data, end=" ")
print(node1.link.data, end=" ")
print(node1.link.link.data, end=" ")
print(node1.link.link.link.data, end=" ")
print(node1.link.link.link.link.data, end=" ")