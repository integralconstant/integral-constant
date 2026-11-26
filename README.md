# 202430205 김진형

[2주차](#0910-강의-내용-2주차) | [3주차](#0917-강의-내용-3주차) | [5주차](#1001-강의-내용-5주차) | [6주차](#1008-강의-내용-6주차) | [7주차](#1015-강의-내용-7주차) | [9주차](#1029-강의-내용-9주차) | [10주차](#1105-강의-내용-10주차) | [11주차](#1112-강의-내용-11주차) | [12주차](#1119-강의-내용-12주차) | [13주차](#1126-강의-내용-13주차)

## 1126 강의 내용 (13주차)

### **재귀**

#### - 재귀 알고리즘
동일한 작동을 무한 반복하는 알고리즘

#### - 재귀 호출
자기 자신을 다시 호출하는 것 <br>
무한히 반복하기에 반환 조건을 줘야 한다

#### - 실습
- 26-11-26
    - open_box.py
    - sum_number.py
    - factorial.py
    - print_star.py
    - count_down.py
    - gugu.py
    - power_n.py
    - sum_array.py
    - fibonacci.py

## 1119 강의 내용 (12주차)

### **그래프**

그래프는 정점(Vertex)과 정점들을 연결하는 간선(Edge)의 집합으로 이루어진 자료구조이다. 네트워크, 도로, 관계 등을 표현할 때 사용한다.

#### - 그래프의 개념

- 정점(Vertex): 그래프를 구성하는 요소이다.
- 간선(Edge): 정점과 정점 사이의 연결이다.
- 인접 정점: 간선으로 직접 연결된 정점이다.

#### - 무방향 그래프

간선에 방향이 없으며 양방향으로 이동할 수 있다. 간선 `(A, B)`는 `A`와 `B`가 서로 연결되어 있음을 의미한다.

#### - 방향 그래프

간선에 방향이 있어 한쪽 정점에서 다른 정점으로만 이동할 수 있다. 간선 `(A, B)`는 `A에서 B로 이동`할 수 있음을 의미한다.

#### - 가중치 그래프

간선마다 거리, 비용, 시간 등의 가중치가 있다.

---

### 그래프의 순회

그래프의 순회는 시작 정점에서 연결된 모든 정점을 한 번씩 방문하는 것이다. 이미 방문한 정점은 다시 방문하지 않도록 방문 여부를 기록한다.

#### - 깊이 우선 탐색(DFS)

한 경로를 가능한 끝까지 탐색한 뒤, 다른 경로로 돌아와 탐색한다. 일반적으로 스택이나 재귀를 사용한다.

#### - 너비 우선 탐색(BFS)

시작 정점과 가까운 정점을 먼저 방문한 뒤 다음 레벨의 정점을 차례로 방문한다. 일반적으로 큐를 사용한다.

---

###  인접 행렬 표현

인접 행렬은 정점의 개수가 `N`개일 때 `N x N` 크기의 2차원 배열로 그래프를 표현하는 방식이다.

- 행과 열은 각각 정점을 나타낸다.
- 행은 출발 정점, 열은 도착 정점을 나타낸다.

#### - 무방향 그래프

정점 `A, B, C`에서 간선이 `A-B`, `A-C`일 때, 양방향으로 이동 가능하므로 대칭 인접 행렬로 표현한다.

```text
     A  B  C
A   0  1  1
B   1  0  0
C   1  0  0
```

#### - 방향 그래프

정점 `A, B, C`에서 간선이 `A→B`, `C→A`일 때, 방향이 있는 만큼 행에서 열로만 이동 가능하도록 `1`을 표시한다.

```text
     A  B  C
A   0  1  0
B   0  0  0
C   1  0  0
```

방향 그래프의 인접 행렬은 일반적으로 대칭이 아니다.

---

### 그래프의 정점 생성

그래프의 정점은 인접 행렬의 행과 열에 대응한다. 정점의 개수만큼 행과 열이 같은 크기의 2차원 배열을 만들고, 인접 행렬의 초깃값은 모두 `0`으로 설정한다.

1) 그래프에 사용할 정점 이름과 개수를 정한다.
2) 정점 이름을 배열에 순서대로 저장한다.
3) 정점의 개수 `N`에 대해 `N x N` 크기의 2차원 배열을 만든다.
4) 초기에는 간선이 없으므로 모든 요소를 `0`으로 초기화한다.

예를 들어 정점 `A, B, C`를 생성하면 각 정점은 인접 행렬의 행과 열에 순서대로 대응한다.

```text
정점 목록
[0] A  [1] B  [2] C

      열 0  1  2
         A  B  C
행  0 A  0  0  0
    1 B  0  0  0
    2 C  0  0  0
```

- 행 `0`과 열 `0`은 정점 `A`를 나타낸다.
- 행 `1`과 열 `1`은 정점 `B`를 나타낸다.
- 행 `2`와 열 `2`은 정점 `C`를 나타낸다.
- 배열의 특정 위치는 출발 정점과 도착 정점의 관계를 나타낸다. 예를 들어 `(행 0, 열 1)`은 `A에서 B로 이동 가능한지`를 나타낸다.

---

### 그래프의 구현
```python
class graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
```
#### 깊이 우선 탐색의 구현

인접 행렬에서 시작 정점의 행을 왼쪽부터 확인하며, 연결되어 있고 아직 방문하지 않은 정점으로 이동한다. 더 이상 이동할 곳이 없으면 재귀 호출이 끝나며 이전 정점으로 돌아가 다른 경로를 탐색한다. `visited` 배열은 정점의 중복 방문을 막고, `order`에는 방문 순서를 저장한다.

예를 들어 인접 행렬에 `0-1`, `0-2`, `1-3` 간선이 있고 정점 `0`에서 시작하면 방문 순서는 `[0, 1, 3, 2]`이다. 인접 정점을 확인하는 순서에 따라 결과가 달라질 수 있다.

---

### 최소 신장 트리

신장 트리는 연결된 무방향 그래프의 모든 정점을 포함하면서 사이클이 없는 부분 그래프이다. 정점이 `N`개인 신장 트리는 간선을 `N - 1`개 가진다.

최소 신장 트리(MST)는 가중치 그래프의 신장 트리 중 간선 가중치의 합이 가장 작은 트리이다. 모든 정점을 연결하되 전체 연결 비용을 최소화할 때 사용한다.

#### - 가중치 그래프와 신장 트리

다음 가중치 그래프에는 네 정점과 다섯 간선이 있다.

```text
A-B: 1
A-C: 4
B-C: 2
B-D: 5
C-D: 3
```

모든 정점을 연결하면서 사이클이 생기지 않도록 `A-B`, `B-C`, `C-D`를 선택하면 신장 트리가 된다.

```text
A --1-- B --2-- C --3-- D
```

간선 가중치의 합은 `1 + 2 + 3 = 6`이며, 이 예시의 최소 신장 트리이다.

#### - 프림 알고리즘

임의의 정점에서 시작해 현재 트리에 포함된 정점과 포함되지 않은 정점을 잇는 간선 중 가중치가 가장 작은 간선을 선택한다. 모든 정점이 연결될 때까지 반복한다.

위 예시에서 `A`부터 시작하면 `A-B(1)`, `B-C(2)`, `C-D(3)` 순서로 선택해 최소 신장 트리를 만든다.

#### - 크루스컬 알고리즘

모든 간선을 가중치가 작은 순서로 정렬한 뒤, 사이클을 만들지 않는 간선을 차례로 선택한다. 신장 트리가 완성될 때까지 반복한다.

위 예시에서는 간선을 `A-B(1)`, `B-C(2)`, `C-D(3)`, `A-C(4)`, `B-D(5)` 순으로 살펴본다. 앞의 세 간선을 선택하면 모든 정점이 연결되므로 종료한다.

[to top](#202430205-김진형)

## 1112 강의 내용 (11주차)

### <b>Queue(2)</b>

#### - 큐가 가득 찼는지 확인하기

1) `rear != len(queue) - 1`: 뒤쪽에 빈 칸이 있으므로 데이터를 더 넣을 수 있다.
2) `rear == len(queue) - 1 && front == -1`: rear가 마지막 칸에 있고 아직 삭제한 데이터가 없다. 큐가 가득 찬 상태다.
3) `rear == len(queue) - 1 && front != -1`: 앞쪽에서 데이터를 삭제해 빈 칸이 생겼지만, 선형 큐에서는 그 칸을 재사용할 수 없다. rear가 마지막 칸에 있으므로 더 넣을 수 없다.

선형 큐는 삭제 후 앞쪽 공간을 활용하지 못하는 한계가 있다. 이를 보완하려면 원형 큐를 사용할 수 있다.

###  원형 queue

배열의 마지막 칸 다음을 첫 칸으로 연결해 원형처럼 사용하는 큐이다. `rear`가 끝에 도달하면 처음으로 돌아가므로, 선형 큐와 달리 앞쪽의 빈 공간을 재사용할 수 있다.

아래 조건은 `front`와 `rear`가 모두 0에서 시작하고, 한 칸을 비워 두는 방식이다.

1) `front == rear`: 큐가 비어 있다.
2) `(rear + 1) % len(queue) == front`: 큐가 가득 찼다. 한 칸을 비워 두어 빈 상태와 구분한다.

```python
if front == rear:
    print("큐가 비어있습니다.")
elif (rear + 1) % len(queue) == front:
    print("큐가 가득 찼습니다.")
```

#### - enQueue

가득 찬 상태인지 확인한 뒤 `rear`를 `(rear + 1) % 큐 크기`로 이동시켜 데이터를 저장한다. 선형 큐처럼 `rear`를 단순히 1 증가시키는 대신, 마지막 칸 다음에는 첫 칸으로 돌아가 앞쪽의 빈 공간을 재사용한다.

```python
def enqueue(data):
    global rear
    if (rear + 1) % len(queue) == front:
        print("큐가 가득 찼습니다.")
        return
    rear = (rear + 1) % len(queue)
    queue[rear] = data
```

#### - deQueue

비어 있는 상태인지 확인한 뒤 `front`를 `(front + 1) % 큐 크기`로 이동시켜 데이터를 꺼낸다. 선형 큐와 달리 `front`도 마지막 칸 다음에 첫 칸으로 돌아오며, 추출한 위치는 다음 삽입에서 다시 사용할 수 있다.

```python
def dequeue():
    global front
    if front == rear:
        print("큐가 비어있습니다.")
        return None
    front = (front + 1) % len(queue)
    data = queue[front]
    queue[front] = None
    return data
```

###  **이진 트리**

각 노드가 가질 수 있는 자식 노드의 수가 최대 두 개인 트리이다. 자식은 왼쪽 자식과 오른쪽 자식으로 구분한다.

#### - 트리 자료구조 용어

- 노드(Node), 루트(Root), 간선(Edge)
- 부모(Parent), 자식(Child), 형제(Sibling)
- 리프 노드(Leaf), 차수(Degree), 레벨(Level), 높이(Height)
- 서브트리(Subtree)

#### - 이진 트리의 종류

- **포화 이진 트리**: 모든 레벨에 노드가 가득 찬 이진 트리이다.
- **완전 이진 트리**: 마지막 레벨을 제외한 모든 레벨이 가득 차 있고, 마지막 레벨의 노드는 왼쪽부터 채워진 이진 트리이다.
- **일반 이진 트리**: 각 노드가 자식 노드를 0개, 1개 또는 2개 가질 수 있는 이진 트리이다.
- **편향 이진 트리**: 각 부모 노드가 왼쪽이나 오른쪽 한쪽으로만 자식을 가져 한쪽으로 치우친 이진 트리이다.

#### - 이진 트리의 노드 구조

- 각 노드는 저장할 **데이터**와 **왼쪽 자식**, **오른쪽 자식**을 가리키는 연결 정보를 가진다.
- 자식 노드가 없으면 해당 연결 정보는 비어 있다(`None`).

#### - 이진 트리 구현

```python
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
```

#### - 이진 트리의 순회

순회는 트리의 모든 노드를 정해진 순서에 따라 한 번씩 방문하는 것이다. 아래 트리에서 방문 순서는 다음과 같다.

```text
        1
      /    \
    2       3
  /   \    /
4     5 6 
```

- **전위 순회**: 루트 → 왼쪽 서브트리 → 오른쪽 서브트리 (`1, 2, 4, 5, 3, 6`)
- **중위 순회**: 왼쪽 서브트리 → 루트 → 오른쪽 서브트리 (`4, 2, 5, 1, 6, 3`)
- **후위 순회**: 왼쪽 서브트리 → 오른쪽 서브트리 → 루트 (`4, 5, 2, 6, 3, 1`)
- **레벨 순회**: 위 레벨부터 왼쪽에서 오른쪽 순서로 방문 (`1, 2, 3, 4, 5, 6`)

###  이진 탐색 트리

각 노드가 최대 두 개의 자식을 가지며, 다음과 같은 규칙으로 데이터를 정렬해 저장하는 이진 트리이다.

- 왼쪽 서브트리에는 현재 노드보다 작은 값이 온다.
- 오른쪽 서브트리에는 현재 노드보다 큰 값이 온다.
- 값을 찾거나 삽입할 때 현재 노드와 비교해 왼쪽 또는 오른쪽으로 이동한다.
- 중위 순회하면 데이터를 작은 값부터 순서대로 방문한다.

예를 들어 `5, 3, 7, 2, 4` 순서로 삽입하면 다음과 같이 구성된다.

```text
         5
      /     \
    3       7
  /   \   
2      4 
```

#### - **데이터 삽입**

1) 트리가 비어 있으면 새 노드를 루트로 둔다.
2) 비어 있지 않으면 루트에서 시작해 삽입할 값과 현재 노드의 값을 비교한다.
3) 삽입할 값이 더 작으면 왼쪽으로, 더 크면 오른쪽으로 이동한다.
4) 이동할 자식 노드가 비어 있으면 그 자리에 새 노드를 연결한다. 비어 있지 않으면 해당 자식 노드에서 비교를 반복한다.

같은 값이 이미 있을 때의 처리(삽입하지 않거나 중복을 허용하는 등)는 구현 규칙에 따라 정한다.

#### - **데이터 검색**

1) 루트에서 시작해 찾을 값과 현재 노드의 값을 비교한다.
2) 값이 같으면 검색을 마친다. 찾을 값이 더 작으면 왼쪽으로, 더 크면 오른쪽으로 이동한다.
3) 이동할 자식 노드가 비어 있으면 해당 값은 트리에 없다. 비어 있지 않으면 비교를 반복한다.

예를 들어 `4`를 찾을 때는 `5`보다 작으므로 왼쪽으로 이동하고, `3`보다 크므로 오른쪽으로 이동한다. 그 노드의 값이 `4`이므로 검색을 마친다.

#### - **데이터 삭제**

삭제할 노드를 먼저 검색한 뒤, 자식 노드의 개수에 따라 처리한다.

1) **자식이 없는 경우**: 부모 노드와의 연결을 끊는다.
2) **자식이 하나인 경우**: 부모 노드가 삭제할 노드의 자식을 직접 가리키도록 연결한다. 삭제할 노드가 루트라면 자식 노드가 새 루트가 된다.
3) **자식이 둘인 경우**: 오른쪽 서브트리에서 가장 작은 값(중위 후속자)을 찾아 삭제할 노드의 값과 바꾼 다음, 그 값을 원래 위치에서 삭제한다. 후속자는 왼쪽 자식이 없으므로 자식이 없거나 하나인 경우로 처리할 수 있다.

삭제 후에도 왼쪽에는 작은 값, 오른쪽에는 큰 값이 오는 이진 탐색 트리의 규칙을 유지해야 한다.

#### - 장점

- 정렬된 규칙에 따라 탐색할 범위를 매 단계 줄일 수 있어, 균형이 잘 잡힌 경우 검색·삽입·삭제가 효율적이다.
- 중위 순회만으로 데이터를 작은 값부터 순서대로 확인할 수 있다.
- 노드를 연결하는 구조이므로 필요에 따라 데이터를 삽입하거나 삭제하기 쉽다.

[to top](#202430205-김진형)

## 1105 강의 내용 (10주차)

### - Queue

선입선출, 후입후출 <br>
수평적 구조, 앞뒤로 구분된 출입구가 존재 <br>
ex) 대기열

#### - enQueue

```python
def enqueue(data):
    global rear
    if is_full():
        print("큐가 가득 찼습니다.")
        return
    rear += 1
    test_queue[rear] = data
```

#### - deQueue

```python
def dequeue():
    global front
    if is_empty():
        print("큐가 비어있습니다.")
        return None
    front += 1
    data = test_queue[front]
    test_queue[front] = None
    return data
```

#### 실습코드
```python
def init_queue(size):
    global test_queue, front, rear
    test_queue = [None] * size
    front = -1
    rear = -1
    return print("큐가 초기화되었습니다. 큐 크기는 " + str(size) + "입니다.")

def enqueue(data):
    global rear
    if is_full():
        print("큐가 가득 찼습니다.")
        return
    rear += 1
    test_queue[rear] = data
    
def dequeue():
    global front
    if is_empty():
        print("큐가 비어있습니다.")
        return None
    front += 1
    data = test_queue[front]
    test_queue[front] = None
    return data

def peek_queue():
    global front
    if is_empty():
        print("큐가 비어있습니다.")
        return None
    data = test_queue[front + 1]
    return print("peek된 데이터: " + str(data))

def queue_print():
    print("-----큐 상태-----")
    for i in range(len(test_queue)):
        print(test_queue[i])
    print("-----------------------------")
    print("front: " + str(front))
    print("rear: " + str(rear))
    print("-----------------------------")
    
def is_full():
    global rear
    if rear == len(test_queue) - 1:
        return True
    else:
        return False

def is_empty():
    global front, rear
    if front == rear:
        return True
    else:
        return False
    
init_queue(5)

enqueue("커피")
enqueue("녹차")
enqueue("꿀물")
queue_print()

dequeue()
dequeue()
dequeue()
dequeue()
queue_print()
enqueue("콜라")
print("enqueue 후 큐 상태: ")
queue_print()
peek_queue()
```

[to top](#202430205-김진형)

## 1029 강의 내용 (9주차)

### - Stack

선입후출, 후입선출 <br>
수직적인 구조, 출입구가 하나 <br>
ex) 프링글스 통, 종이컵의 스택

-push: 데이터 삽입<br>
-pop: 데이터 추출<br>
-top: 스택 최상단 데이터
```python
def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    return print("스택이 초기화되었습니다. 스택 크기는 " + str(size) + "입니다.")
    
def is_full():
    global top
    if top == len(stack) -1:
        return print("스택이 가득 찼습니다.")
    else:
        return print("스택이 가득 차지 않았습니다.")
    
def is_empty():
    global top
    if top == -1:
        return True
    else:
        return False
    
def push(data):
    global top
    top += 1
    stack[top] = data
    
def pop():
    global top
    data = stack[top]
    stack[top] = None
    if (is_empty()):
        top -= 1
        return print("스택이 비어있습니다.")
    else:
        top -= 1
        return print("pop된 데이터:" + str(data))

def peek():
    global top
    data = stack[top]
    return print("peek된 데이터: " + str(data))
    
def print_stack():
    print("-----스택 상태-----")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print("-----------------------------")
```

[to top](#202430205-김진형)

## 1015 강의 내용 (7주차)

### - 원형 연결 리스트

node1 -> node2 -> node3 -> node4 -> node5 -> node1 -> ...

- example-01.py

```python
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
node1 = Node()
node1.data = "다현"
node1.link = node1 #항상 마지막 노드가 첫번째 노드를 가리킨다(첫번째 노드가 마지막 노드인 경우도 있다. 따라서 첫 번째 노드에게도 자기 자신으로 링크를 주어야 한다.)

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
```

### - 원형 연결 리스트의 중간 노드 삽입

- example-02.py

```python
# 노드 구조는 example-01.py와 동일

newNode = Node()
newNode.data = "재남"
newNode.link = node2.link
node2.link = newNode

current = node1
print(current.data, end = "")
while current.link != node1:
    current = current.link
    print(current.data, end = "")
```

[to top](#202430205-김진형)


## 1008 강의 내용 (6주차)

### - 단순 연결 리스트의 데이터 관리

- node01.py

```python
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
```
[to top](#202430205-김진형)


## 1001 강의 내용 (5주차)

### - 선형 리스트

- kakao-1.py

```python
kakao = []             # 빈 리스트 생성
kakao.append("다현0")  # 인덱스 0번에 "다현0" 추가
kakao.append("다현1")  # 인덱스 1번에 "다현1" 추가
kakao.append("다현2")  # 인덱스 2번에 "다현2" 추가
kakao.append("다현3")  # 인덱스 3번에 "다현3" 추가
kakao.append("다현4")  # 인덱스 4번에 "다현4" 추가
print(kakao)
kakao.append(kakao[4]) # 인덱스 5번에 4번 인덱스 값 저장
print(kakao)
kakao[4] = kakao[3]    # 인덱스 4번에 3번 인덱스 값 저장
kakao[3] = kakao[2]    # 인덱스 3번에 2번 인덱스 값 저장
kakao[2] = "솔라"      # 인덱스 2번에 "솔라" 저장
print(kakao)
```

### -단순 연결 리스트

- node.py

```python
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

print(node1.data, end=" ")                     # node1
print(node1.link.data, end=" ")                # node1.link=node2
print(node1.link.link.data, end=" ")           # node1.link*2=node3
print(node1.link.link.link.data, end=" ")      # node1.link*3=node4
print(node1.link.link.link.link.data, end=" ") # node1.link*4=node5
```
[to top](#202430205-김진형)

---

 ## 0917 강의 내용 (3주차)
 
 -  kakao.py

```python
kakao = ["가나", "다라", "마바", "사아", "자차"]
print(kakao)
kakao.append(None)
print(kakao)
kakao[5] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[3]
kakao[3] = None
print(kakao)
kakao[3] = "삽입"
print(kakao)
```
[to top](#202430205-김진형)

---

 ## 0910 강의 내용 (2주차)
 
 # html의 h1부터 h6까지 푸시
 # h1크기
 ## h2 크기
 ### h3 크기
 #### h4 크기
 ##### h5 크기
 ###### h6 크기

 *이텔릭체*

 **볼드**

 ***이텔릭+볼드***

  ~~취소선~~

  ---

  1. 사과
  2. 배
  3. 감

- 사과
    - 청사과
    - 풋사과
        - ㅁㄴㅇㄹ
- 배
- 감

## 코드 블럭
```python
# This program prints Hello, world!
print(Hello world!)
```

```Java
public class Main {
    public static void main(String[] args){
        System.out.println("Hello Java!");
    }
}
```

## 링크

[구글 바로가기](https://www.google.com "alt 옵션")

[이름](#202430205-김진형)

[내부링크](#html의-h1부터-h6까지-푸시)

## 이미지 삽입
![구글 로고](26-09-10\image.png "google logo")

[to top](#202430205-김진형)