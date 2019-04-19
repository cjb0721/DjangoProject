from django.contrib import admin
from .models import Question, Select
# Register your models here.


class SelectInline(admin.StackedInline):
    model = Select
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [SelectInline, ]
    list_display = ['desctext', ]
    list_per_page = 5
    search_fields = ['text', ]


class SelectAdmin(admin.ModelAdmin):
    list_display = ['choice', 'votes', ]
    list_filter = ['item', ]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Select, SelectAdmin)