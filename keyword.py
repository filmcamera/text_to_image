'''
import nltk
download('punkt')
'''
from nltk import *

# .txt 파일을 string으로 저장, 줄 바꿈은 공백으로 대체
with open('1.txt', 'r') as file:
    txt = file.read().replace('\n', ' ')

# 모두 소문자로 변경
txt = txt.lower()

# txt 파일을 토큰화 한 다음 universal part of speech tagset 적용
txt_tokens = pos_tag(word_tokenize(txt), tagset='universal')

# 명사와 형용사 태그의 토큰들만 모아 리스트를 만듦
txt_noun_list = [word for word, pos in txt_tokens if pos in ['NOUN']]
txt_adj_list = [word for word, pos in txt_tokens if pos in ['ADJ']]
#print(txt_noun_list)
fd_noun = FreqDist(txt_noun_list)
fd_adj = FreqDist(txt_adj_list)

print(fd_noun.most_common(20))
print("\n")
print(fd_adj.most_common(20))