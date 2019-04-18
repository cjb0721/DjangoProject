from django.contrib import admin
from .models import Question, Select
# Register your models here.

admin.site.register(Question)
admin.site.register(Select)