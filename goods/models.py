# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import secrets
import uuid  # Added this line

def generate_uuid():
    return secrets.token_hex(4)  # Increased length for better uniqueness

class goods(models.Model):
    GOODS_TYPES = [
        ('Electronics', 'Electronics'),
        ('Apparel', 'Apparel'),
        ('Pharmaceuticals', 'Pharmaceuticals'),
        ('Cosmetics', 'Cosmetics'),
        ('Books', 'Books'),
        ('Home Goods', 'Home Goods'),
        ('Food Items', 'Food Items'),
        ('Documents', 'Documents'),
        ('Sporting Goods', 'Sporting Goods'),
        ('Toys', 'Toys'),
        ('Automotive Parts', 'Automotive Parts'),
        ('Miscellaneous', 'Miscellaneous'),  # Default category
    ]
    goods_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goods_name = models.CharField(max_length=255,)
    goods_cost = models.CharField(max_length=20, default="")
    goods_type = models.CharField(max_length=255, choices=GOODS_TYPES, default='Miscellaneous')
    goods_sender_name = models.CharField(max_length=255, default="")
    goods_sender_mobile = models.CharField(max_length=20, default="")
    goods_sender_email = models.EmailField(max_length=255, default="")
    goods_sender_address = models.TextField(default="")
    goods_receiver_name = models.CharField(max_length=255, default="")
    goods_receiver_mobile = models.CharField(max_length=20, default="")
    goods_receiver_email = models.EmailField(max_length=255, default="")
    goods_receiver_address = models.TextField(default="")
    goods_description = models.TextField(default="")

    def __str__(self):
        return self.goods_name