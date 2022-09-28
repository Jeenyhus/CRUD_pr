from django.db import models

# Create your models here.
class Item(models.Model):
    iid = models.CharField(max_length=5)
    iname = models.CharField(max_length=30)

    def __str__(self):
        return self.iname