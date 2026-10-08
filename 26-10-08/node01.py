# Node class 생성
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

# 데이터 삽입
newNode = Node()            # 새 노드 생성
newNode.data = "솔라"       # 새 노드에 데이터 할당
newNode.link = node2.link   # 새 노드의 링크를 기존 노드의 링크로 설정
node2.link = newNode        # 기존 노드의 링크를 새 노드로 변경

# 데이터 삭제
node4.link = node5.link     # node4의 링크를 node5의 링크로 설정
del(node5)                  # node5 삭제

# 모든 데이터 출력
current = node1             # 첫 번째 노드를 current에 할당
print(current.data, end=" ") 
while current.link != None: # current.link가 None이 아닌 동안 반복
    current = current.link  # current를 다음 노드로 이동
    print(current.data, end=" ")