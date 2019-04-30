from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    num = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    pub_com = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Borrows(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_borrow = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name+"被"+self.user.name+"借出"


class HotPic(models.Model):
    name = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='hotpic')
    index = models.SmallIntegerField(unique=True)

    def __str__(self):
        return self.name


class MessInfo(models.Model):
    title = models.CharField(max_length=20)
    # 富文本编辑器字段
    message = HTMLField()

    def __str__(self):
        return self.title


