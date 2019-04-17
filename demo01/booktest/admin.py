from django.contrib import admin
from .models import *

# Register your models here.


class HeroInline(admin.StackedInline):
    model = Hero
    # 关联个数
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [HeroInline, ]


# admin.site.register(Book)
admin.site.register(Book, BookAdmin)


class HeroAdmin(admin.ModelAdmin):
    # 后台显示控制
    # 显示对象指定列 列名与模型中一致
    list_display = ['hname', 'hsex', 'hcontent']
    # 过滤规则 列名一致
    list_filter = ['name', 'gender']
    # 显示搜索字段 支持模糊查询
    search_fields = ['name', 'content']
    # 分页 每页显示个数
    list_per_page = 3


# 注册模型类
admin.site.register(Hero, HeroAdmin)


"""
少量代码管理强大后台

需要将特定数据模型注册才能后台管理

"""

