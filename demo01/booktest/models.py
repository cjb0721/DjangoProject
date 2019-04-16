from django.db import models

# Create your models here.


class Book(models.Model):
    book_title = models.CharField(max_length=20)
    book_pubdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    content = models.CharField(max_length=50)
    # 外键 第一个参数：关联的表名 第二个参数：删除类型
    book = models.ForeignKey("Book", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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

"""
shell命令测试：
进入shell命令： python manage.py shell  不需要运行项目就可以操作数据库
导入类： from booktest.models import *
查找所有行 表名.objects.all()
根据主键查找 表名.objects.get(pk=主键名)
添加对象到数据库 对象.save()
修改对象到数据库 对象.列名=修改的值  对象.save()
删除 对象.delete()

若存在一对多关系： 一方.多方类名全小写_set.all() 可查询相应信息

类名.objects.create(列名=值)  不需要save()
"""


