from django.db import models

# Create your models here.


class Temp1Manage(models.Manager):
    def create_temp11(self, _name, _age):
        temp1 = self.model()
        temp1.name = _name
        temp1.age = _age
        temp1.save()

    def create_temp111(self,  _name, _age):
        return self.create(name=_name, age=_age)


# 使用模型创建对象 三种方法
class Temp1(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    manage1 = models.Manager()
    manage2 = Temp1Manage()

    # 1、使用类方法创建
    @classmethod
    def create_temp1(cls, _name, _age):
        return cls(name=_name, age=_age)


# 一对一 A、B
class A(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class B(models.Model):
    name = models.CharField(max_length=20)
    b_a = models.OneToOneField(A, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 多对多 Host、Apps
class Apps(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=50)
    Host_App = models.ManyToManyField(Apps)

    def __str__(self):
        return self.name



