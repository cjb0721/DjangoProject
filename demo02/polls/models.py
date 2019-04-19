from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def desctext(self):
        return self.text
    desctext.short_description = '问题描述'


class Select(models.Model):
    item = models.CharField(max_length=20)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.item

    def choice(self):
        return self.item
    choice.short_description = '问题选项'

    def votes(self):
        return self.vote
    votes.short_description = '投票数'


