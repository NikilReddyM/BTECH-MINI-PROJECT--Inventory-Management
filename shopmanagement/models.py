from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
    product_name = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=1,default='A')
    price_per_piece = models.PositiveIntegerField(default=0)
    min_count = models.PositiveIntegerField(default=5)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.product_name
