import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('./model_word2vec_min100.txt',binary=False)


def vac_detail(word):
    print(f'{word}の特徴量のベクトル')
    print(model[word])
    print(model[word].shape)

def vac_similar(positive=None, negative=None):
    if positive is not None:
        print(*positive, sep=" + ", end=" ")
    if negative is not None:
        print("-", end=" ")
        print(*negative, sep=" - ", end=" ")
    print("\n")
    results = model.most_similar(positive=positive, negative=negative)
    for result in results:
        print(result)

# word = '人生'
# vac_detail(word)

positive=['学生', '学会']
negative=None
vac_similar(positive=positive, negative=negative)