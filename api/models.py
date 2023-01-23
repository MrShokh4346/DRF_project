from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Books(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    class Meta:
        verbose_name_plural = 'Books'
    def __str__(self):
        return self.name