from django.contrib import admin

from article.models import News, Newsletter


admin.site.register(News)
admin.site.register(Newsletter)