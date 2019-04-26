from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    num = models.IntegerField()
    email = models.EmailField()

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
        return self.book, self.user



