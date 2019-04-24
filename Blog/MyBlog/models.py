from django.db import models

# Create your models here.


class ArticleSort(models.Model):
    sort = models.CharField(max_length=50)

    def __str__(self):
        return self.sort


class Label(models.Model):
    tag_name = models.CharField(max_length=20)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    abstract = models.CharField(max_length=200)
    read_num = models.IntegerField(default=0)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    sort = models.ForeignKey(ArticleSort, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Label)

    def __str__(self):
        return self.title


class Comment(models.Model):
    commentator = models.CharField(max_length=20)
    email = models.EmailField()
    url = models.URLField()
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.commentator






