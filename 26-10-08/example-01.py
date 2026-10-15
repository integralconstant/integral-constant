class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
node1 = Node()
node1.data = "다현"
node1.link = node1 #항상 마지막 노드가 첫번째 노도를 가리킨다

node2 = Node()
node2.data = "정연"
node1.link = node2 #노드 1 -> 노드 2
node2.link = node1 #노드 2 -> 노드 1

node3 = Node()
node3.data = "쯔위"
node2.link = node3 # 노드 2 -> 노드 3
node3.link = node1 # 노드 3 -> 노드 1

node4 = Node()
node4.data = "사나"
node3.link = node4 # 노드 3 -> 노드 4
node4.link = node1 # 노드 4 -> 노드 1

node5 = Node()
node5.data = "지효"
node4.link = node5 # 노드 4 -> 노드 5
node5.link = node1 # 노드 5 -> 노드 1

current = node1
print(current.data, end = "")
while current.link != node1:
    current = current.link
    print(current.data, end = "")