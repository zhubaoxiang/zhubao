from django.db import models

# Create your models here.
from django.db import models


class BaoModel(models.Model):
    age = models.IntegerField()
    address = models.CharField(max_length=200)


class ComModel(models.Model):
    """
    class com
    """
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField()
    port = models.IntegerField()
    bao = models.ForeignKey(BaoModel, related_name='BAO', on_delete=models.DO_NOTHING, default=1)


class ZhuModel(models.Model):
    """
    class com
    """
    name = models.ForeignKey(ComModel, related_name='ZHU', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'zhumodel'
