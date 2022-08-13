from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import ShortURL

admin.site.register(ShortURL)

class URLShortenerAdminSite(AdminSite):
    title_header = "Shortener Admin"
    site_header = "URL Shortener Admin"
    index_title = "URL Shortener Admin"

admin_site = URLShortenerAdminSite(name="urlshortener")