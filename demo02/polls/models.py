from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Select(models.Model):
    item = models.CharField(max_length=20)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.item

