kakao = []
kakao_len = len(kakao)
print(kakao_len)
kakao.append("다현0")
kakao.append("다현1")
kakao.append("다현2")
print(kakao)
kakao_len = len(kakao)
print(kakao_len)
print(kakao[0])
print(kakao[kakao_len - 1]) # = print(kakao[2])
#kakao.append("다현3")
kakao.append(None)
print(kakao)
#kakao[3] = "다현3"
kakao[len(kakao) - 1] = "다현3"
print(kakao)