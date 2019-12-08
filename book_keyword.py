from nltk import *

# playlist.txt 파일에서 가수와 제목을 가져옴
with open('book.txt', 'r') as f:
    b = f.read().replace('\n', ' ')

splited_by_chapter = list()
splited_by_chapter = b.split('Chapter')
del splited_by_chapter[0]
#print(splited_by_chapter)

ch = 1
for i in splited_by_chapter :
    print('chapter', ch)
    ch += 1

    # lyric 문자열을 토큰화 한 다음 universal 품사 tagset 적용
    lyric_tokens = pos_tag(word_tokenize(i))

    # 명사, 형용사 태그의 토큰들만 모아 각각 리스트를 만듦
    lyric_noun_list = [word for word, pos in lyric_tokens if pos in ['NN' or 'NNP']]
    lyric_adj_list = [word for word, pos in lyric_tokens if pos in ['JJ']]

    # 길이 3 미만의 단어는 제외
    lyric_noun_list = [word for word in lyric_noun_list if not len(word) < 3]
    lyric_adj_list = [word for word in lyric_adj_list if not len(word) < 3]

    # (키워드, 빈도수) 튜플을 원소로 가지는 리스트를 생성
    fd_noun = FreqDist(lyric_noun_list)
    fd_adj = FreqDist(lyric_adj_list)

    # 가장 높은 빈도수 3개의 리스트를 생성 후 출력
    print(fd_noun.most_common(3))
    print(fd_adj.most_common(3))
