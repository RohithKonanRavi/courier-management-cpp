# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from goods.models import goods

class Tracking(models.Model):
    goods = models.ForeignKey(goods, to_field='goods_id', on_delete=models.CASCADE, related_name='trackings')
    location = models.CharField(max_length=200)
    tracking_date = models.DateTimeField(default=timezone.now)
    tracking_description = models.TextField(default="No updates yet.")  # More informative default

    def __str__(self):
        return f"Tracking record for {self.goods.goods_name} at {self.location}"
    
    
