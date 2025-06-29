from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path("admin/defender/", include("defender.urls")),
    path("admin/", admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
