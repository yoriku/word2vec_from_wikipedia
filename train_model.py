from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
from gensim.models import word2vec

# サンプルテキストデータ
sentences = word2vec.Text8Corpus('./wiki_wakati.txt')
print("start...")

# Word2Vecモデルのトレーニング
vectors = Word2Vec(sentences, vector_size=100, window=5, seed=1, workers=12, min_count=10)
vectors.wv.save_word2vec_format('model_word2vec.txt')