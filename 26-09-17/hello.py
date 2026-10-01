#index     0       1       2       3       4
kakao = ["가나", "다라", "마바", "사아", "자차"]
print(kakao)
kakao[2] = None
print(kakao)
kakao[2] =kakao[3]
kakao[3] = None
print(kakao)
kakao[3] = kakao[4]
kakao[4] = None
print(kakao)