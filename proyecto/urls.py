from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from proyecto import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   url(r'^admin/', include(admin.site.urls)),
   url(r'', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
