from django import template
from ..models import *


register = template.Library()


@register.simple_tag
def datelist():
    dates = Article.objects.dates("pub_date", "month", order="DESC")[:3]
    return dates


@register.simple_tag
def sortlist():
    sorts = ArticleSort.objects.all()
    return sorts


@register.simple_tag
def labellist():
    labels = Label.objects.all()
    return labels




