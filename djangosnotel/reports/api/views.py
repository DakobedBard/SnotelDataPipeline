# from elasticsearch import Elasticsearch, RequestsHttpConnection
# from rest_framework_elasticsearch import es_views, es_pagination, es_filters
# from reports.search_indexes import  ReportIndex
#
# # class BlogView(es_views.ListElasticAPIView):
# #     es_client = Elasticsearch(hosts=['elasticsearch:29200/'],
# #                               connection_class=RequestsHttpConnection)
# #     es_model = BlogIndex
# #     es_filter_backends = (
# #         es_filters.ElasticFieldsFilter,
# #         es_filters.ElasticSearchFilter
# #     )
# #     es_filter_fields = (
# #         es_filters.ESFieldFilter('tag', 'tags'),
# #     )
# #     es_search_fields = (
# #         'after.trip_report'
# #
# #     )
#
#
#
# class ReportView(es_views.ListElasticAPIView):
#     es_client = Elasticsearch(hosts=['elasticsearch:29200/'],
#                               connection_class=RequestsHttpConnection)
#     es_model = ReportIndex
#     es_filter_backends = (
#         es_filters.ElasticFieldsFilter,
#         es_filters.ElasticSearchFilter
#     )
#     es_filter_fields = (
#         es_filters.ESFieldFilter('tag', 'tags'),
#     )
#     es_search_fields = (
#         'after.trip_report'
#     )
#
