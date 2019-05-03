from elasticsearch import Elasticsearch

class Data():

    def __init__(self):
        self.es = Elasticsearch("elasticsearch:9200")
        self.index = "sample"

    def search(self):

        res = self.es.search(index=self.index,  body={"query": {"match_all": {}}}, size=10000)
        return res

    def register(self, category, title, contents):

        document = {}
        
        document["category"] = category
        document["title"]    = title
        document["contents"] = contents

        res = self.es.index(index=self.index, doc_type=self.index, body=document)

        return res