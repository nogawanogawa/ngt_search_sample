import numpy as np
from data import Data
from sudachi_analizer import SudachiAnalizer
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class Trainer():

    MODEL_DIR = 'entity_vector/entity_vector.model.txt'

    def __init__(self):
        self.data = Data()
        self.sudachi_analizer = SudachiAnalizer()
        self.model = KeyedVectors.load_word2vec_format(self.MODEL_DIR, binary=False)
        self.vectorizer = TfidfVectorizer(tokenizer=self.sudachi_analizer.get_token, max_df=1.0, min_df=0.5, max_features=10000)

    def get_corpus(self):
        result = self.data.search()
        hits = result["hits"]["hits"]

        category = []
        title = []
        contents = []
        for x in hits:
            category.append(x["_source"]["category"])
            title.append(x["_source"]["title"])
            contents.append(x["_source"]["contents"])

        return category, title, contents

    def train(self):
        # category, title, contents : List[str]
        category, title, contents = self.get_corpus()

        train_matrix = self.vectorizer.fit_transform(contents)

        feature_names = self.vectorizer.get_feature_names()

        new_feature_names = []

        for word in feature_names:
            if word in self.model.wv:
                new_feature_names.append(word)
            else :
                new_feature_names.append('は')
        feature_names = new_feature_names

        v = np.asarray([self.model.wv[word] for word in feature_names])
        doc_title_vectors = (train_matrix @ v) / train_matrix.sum(axis=1)
        
        return category, title, doc_title_vectors


if __name__ == "__main__":
    trainer = Trainer()
    category, title, doc_title_vectors = trainer.train()
    np.savetxt("vector.tsv", doc_title_vectors, delimiter="\t", fmt='%f')
    doc = pd.Series(category, index=title)
    doc.to_csv("metadata.tsv", sep='\t', header=True)
