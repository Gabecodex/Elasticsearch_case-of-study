# Import the Elasticsearch library
from elasticsearch import Elasticsearch

# Connect to an Elasticsearch cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Index a document into the "my_index" index
es.index(index='my_index', body={
    'title': 'Elasticsearch Example',
    'body': 'This is an example of using Elasticsearch in Python.'
})

# Search for the document using the search API
result = es.search(index='my_index', body={
    'query': {
        'match': {
            'body': 'example'
        }
    }
})

# Print the search result
print(result['hits']['hits'])