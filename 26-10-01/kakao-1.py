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