from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, Index, fields, Integer, Text, Keyword, Date, Boolean

# class BlogIndex(Document):
#
#     pk = Integer()
#     title = Text(fields={'raw': Keyword()})
#     created_at = Date()
#     body = Text()
#     tags = Keyword(multi=True)
#     is_published = Boolean()
#
#     class Meta:
#         index = 'blog'
# BlogIndex.init()

class ReportIndex(Document):

    pk = Integer()
    title = Text(fields={'raw': Keyword()})
    created_at = Date()
    body = Text()
    tags = Keyword(multi=True)
    class Meta:
        index = 'db.snowpack.trip_reports'



#
# BlogIndex.init()
ReportIndex.init()