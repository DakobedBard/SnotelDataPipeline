from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('snowpack/', include('snowpack.api.urls')),

    # Upload

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
