# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
#
# from reports.api import documents as reports_documents
#
#
# class ReportDocumentSerializer(DocumentSerializer):
#     class Meta:
#         document = reports_documents.ArticleDocument
#         fields = (
#             'id',
#             'title',
#             'body',
#             'author',
#             'created',
#             'modified',
#             'pub_date',
#         )

from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from reports.models import Blog
# class ElasticBlogSerializer(ElasticModelSerializer):
#     class Meta:
#         model = Blog
#         es_model = BlogIndex
#         fields = ('id_', 'title', 'created_at', 'tags', 'body', 'is_published')
from reports.search_indexes import ReportIndex

class ElasticBlogSerializer(ElasticModelSerializer):
    class Meta:
        model = ReportIndex
        fields = ('id_', 'after')
