from django.contrib import admin
from django.urls import include, path
from pybo.views import base_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import photo_upload

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('upload/', photo_upload, name='photo_upload'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = 'common.views.page_not_found'
