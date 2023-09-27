from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    
    word_list = [] # 사전
    for i in range(1, 6):
        for j in product(words,repeat=i): # 중복 순열을 이용해 가능한 모든 단어 저장
            word_list.append(list(j))
    word_list.sort() # 사전순으로 정렬
    
    # 몇 번째 단어인지 찾기
    for idx, w in enumerate(word_list):
        if word == ''.join(w):
            return idx+1