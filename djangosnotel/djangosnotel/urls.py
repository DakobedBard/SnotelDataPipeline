from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("reports",include("reports.api.urls"))
    # path('snowpack/', include('snowpack.api.urls')),
    # path('reports/', include('reports.api.urls')),
    # Upload

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
