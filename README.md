# 202430205 김진형

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
![구글 로고](image.png "google logo")