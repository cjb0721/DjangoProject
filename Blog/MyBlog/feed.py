from django.contrib.syndication.views import Feed
from .models import *
from django.shortcuts import reverse


class ArticleFeed(Feed):
    """
        RSS 将网站包装成XML格式
        可通过RSS聚合工具订阅，该工具会返回RSS订阅更新的内容
        优点：不需要每次进入博客查看更新
    """

    title = "文章"
    description = "摘要"
    link = "/"

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract

    def item_link(self, item):
        return reverse('MyBlog:single', args=(item.id, ))


