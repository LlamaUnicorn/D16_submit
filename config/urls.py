from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from ckeditor_uploader import views as ckeditor_views

from mmotavern.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('mmotavern/', include('mmotavern.urls')),
    path('auth/', include('authentication.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
