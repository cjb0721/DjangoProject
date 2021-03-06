from django import template
from ..models import *
from comment.models import *
from django.core.paginator import *


register = template.Library()


@register.simple_tag
def datelist():
    dates = Article.objects.dates("pub_date", "month", order="DESC")[:3]
    # print(dates, type(dates))
    return dates


@register.simple_tag
def sortlist():
    sorts = ArticleSort.objects.all()
    return sorts


@register.simple_tag
def labellist():
    labels = Label.objects.all()
    return labels


@register.simple_tag
def commentslist():
    comments = Comments.objects.all()
    print(comments.article)
    return comments


@register.simple_tag
def newarticlelist():
    newarticle = Article.objects.all().order_by('-pub_date')
    return list(newarticle)[:3]


