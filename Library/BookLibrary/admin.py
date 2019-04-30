from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Users)
admin.site.register(Books)
admin.site.register(Borrows)
admin.site.register(HotPic)
admin.site.register(MessInfo)

