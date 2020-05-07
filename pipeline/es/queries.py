from pipeline.utils.elasticsearchConnection import connect_elasticsearch

def query_trip_reports_for_keyword(word):
    es = connect_elasticsearch()
    search_param = {
        "query": {
            "match": {
                "after.trip_report": word
            }
        }
    }
    response = es.search(index="db.snowpack.trip_reports", body=search_param)
    print("Got %d Hits:" % response['hits']['total']['value'])
    return response['hits']
hits = query_trip_reports_for_keyword('snow')
## I was able to query for a particular title of a trip using this query


def query_trip_reports_for_multiple_keywords(word1, word2):
    es = connect_elasticsearch()
    search_param = {
        "query": {
            'bool': {
                'must': [{
                    'match': { 'after.trip_report': word1}
                },{
                    'match': { 'after.trip_report': word2 }
                }]
            }
        }
    }
    response = es.search(index="db.snowpack.trip_reports", body=search_param)
    print("Got %d Hits:" % response['hits']['total']['value'])
    return response['hits']
hits = query_trip_reports_for_multiple_keywords('snow','ice')

def query_trip_reports_for_word1_withouth_word2(word1, word2):
    es = connect_elasticsearch()
    search_param = {
        "query": {
            'bool': {
                'must': {
                    'match': {'after.trip_report': word1}
                },
                'must_not': {
                    'match': {'after.trip_report': word2}
                }
            }
        }
    }
    response = es.search(index="db.snowpack.trip_reports", body=search_param)
    print("Got %d Hits:" % response['hits']['total']['value'])
    return response['hits']
hits = query_trip_reports_for_word1_withouth_word2('snow','ice')


def query_trip_names(name):
    es = connect_elasticsearch()
    search_param = {
        "query": {
            "match": {
                "after.trip_name": name
            }
        }
    }

    response = es.search(index="db.snowpack.trip_reports", body=search_param)
    print("Got %d Hits:" % response['hits']['total']['value'])
    return response['hits']

query_trip_names('Cowiche Canyon')