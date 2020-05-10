from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, GeoPoint, Boolean

class BlogIndex(Document):
    pk = Integer()
    title = Text(fields={'raw': Keyword()})
    created_at = Date()
    body = Text()
    tags = Keyword(multi=True)
    is_published = Boolean()
    location = GeoPoint()

    class Index:
        name = 'blog'