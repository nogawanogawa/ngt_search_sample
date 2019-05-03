from ngt import base as ngt
import numpy
import time
import pandas as pd
from gensim.models.keyedvectors import KeyedVectors

#doc_vectors = KeyedVectors.load_word2vec_format('vector', binary=False)
df = pd.read_csv("vector.tsv",  delimiter='\t')

#word_vectors.init_sims()

#start = time.time()
#result = word_vectors.similar_by_word(u'[ヤマハ]', topn=10)
#print('search time: {:.2f}[sec]'.format(time.time() - start))
#for (word, dist) in result:
#   print('{}\t{:.6f}'.format(word, dist))

index = ngt.Index.create(b'w2vIndex', dimension=200)

#start = time.time()
#for vector in word_vectors.syn0:
for index_, row in df.iterrows():
    vector = row.values
    normalized_vector = vector / numpy.linalg.norm(vector)
    index.insert_object(normalized_vector.tolist())
#print('insert data time:{:.2f}[sec]'.format(time.time() - start))
#start = time.time()
index.build_index()
#print('build index time:{:.2f}[sec]'.format(time.time() - start))

#start = time.time()
index.save()
#print("write index time:{:.2f}[sec]".format(time.time() - start))

del index