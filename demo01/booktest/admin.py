from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Hero)


"""
少量代码管理强大后台

需要将特定数据模型注册才能后台管理

"""

