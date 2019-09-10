from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Rest API Document')

urlpatterns = [
    path(r'doc/', schema_view),
    path(r'admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'auth/', include('auth.urls')),
]
