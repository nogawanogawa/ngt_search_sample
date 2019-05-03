from data import Data
from os import listdir, path

PATH = "text/"

#  pathの中のdir(txt以外)をlistにして返す
def corpus_subdirs(path):
    subdirs = []
    for x in listdir(path):
        if not x.endswith('.txt'):
            subdirs.append(x)
    return subdirs

# pathの中のファイルをlistにして返す
def corpus_filenames(path):
    labels = [] # *.txt
    for y in listdir(path):
        if not y.startswith('LICENSE'):
            labels.append(y)
    return labels

if __name__ == "__main__":
    data = Data()

    for dir in corpus_subdirs(PATH):
        for file in corpus_filenames(PATH+dir):
            corpus_data = open(path.join(PATH + dir + "/" + file), "r")
            source = corpus_data.read()
            data.register(dir, file, source)