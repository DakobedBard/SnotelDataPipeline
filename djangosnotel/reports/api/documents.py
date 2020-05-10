# from elasticsearch_dsl import analyzer
# from django_elasticsearch_dsl import Document, Index, fields
#
# from reports.api import documents as report_documents
# from reports.models import Report
#
# article_index = Index('reports')
# article_index.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )
#
# html_strip = analyzer(
#     'html_strip',
#     tokenizer="standard",
#     filter=["standard", "lowercase", "stop", "snowball"],
#     char_filter=["html_strip"]
# )
#
# @article_index.doc_type
# class ReportDocument(Document):
#     """Article elasticsearch document"""
#
#     id = fields.IntegerField(attr='id')
#     title = fields.TextField(
#         analyzer=html_strip,
#         fields={
#             'raw': fields.TextField(analyzer='keyword'),
#         }
#     )
#     body = fields.TextField(
#         analyzer=html_strip,
#         fields={
#             'raw': fields.TextField(analyzer='keyword'),
#         }
#     )
#     author = fields.IntegerField(attr='author_id')
#     created = fields.DateField()
#     modified = fields.DateField()
#     pub_date = fields.DateField()
#
#     class Meta:
#         model = Report