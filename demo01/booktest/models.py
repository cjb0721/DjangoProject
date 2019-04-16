from django.db import models

# Create your models here.


class Book(models.Model):
    book_title = models.CharField(max_length=20)
    bool_pubdate = models.DateTimeField(auto_now_add=True)


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    content = models.CharField(max_length=50)
    # 外键 第一个参数：关联的表名 第二个参数：删除类型
    book = models.ForeignKey("Book", on_delete=models.CASCADE)


"""
Django框架MVT模式中M
ORM 对象中的O
需要定义实体类

1、定义模型，继承models.Model
2、配置数据库，默认sqlite
3、将apps.py应用名添加到settings.py的INSTALLED_APPS应用列表中
4、生成迁移文件 python manage.py makemigrations
5、执行迁移 python manage.py migrate



"""
