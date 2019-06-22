from django.db import models

# Create your models here.


class Area(models.Model):
    title = models.CharField(max_length=20)
    parrent_area = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

