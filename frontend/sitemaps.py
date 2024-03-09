from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['frontend:home', 'frontend:services', 'frontend:all_services', 'frontend:all_departments', ]

    def location(self, item):
        return reverse(item)
