from django.contrib import admin
from .models import *
# Register your models here.


class ArticlAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pub_date']
    list_filter = ['author', 'sort']
    list_per_page = 4
    search_fields = ['title', 'author', 'sort']


admin.site.register(ArticleSort)
admin.site.register(Article, ArticlAdmin)
admin.site.register(Comment)
admin.site.register(Label)

