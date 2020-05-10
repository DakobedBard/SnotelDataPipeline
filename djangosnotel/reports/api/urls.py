# from rest_framework.routers import SimpleRouter
#
# from reports.api import views
#
# app_name = 'articles'
#
# router = SimpleRouter()
# router.register(
#     prefix=r'',
#     base_name='reports',
#     viewset=views.ArticleViewSet
# )
# urlpatterns = router.urls


from reports.api.views import BlogView
from django.urls import path

urlpatterns = [
    path(r'', BlogView.as_view(), name='list'),
]