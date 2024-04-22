
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from frontend.sitemaps import StaticViewSitemap

from denmark import settings_dev

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('frontend.urls', namespace="frontend")),
                  path('tinymce/', include('tinymce.urls')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemaps'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'frontend.views.error_404_view'
handler500 = 'frontend.views.error_500_view'
handler403 = 'frontend.views.error_403_view'

if settings_dev.DEBUG:
    urlpatterns += static(settings_dev.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)

admin.site.index_title = "Denmark Government Admin"
admin.site.site_header = "Denmark Government"
