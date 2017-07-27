# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_register_app.models import User

class ItemManager(models.Manager):
  def validate(self, form_data):
    errors = []

    if len(form_data['name']) == 0:
      errors.append('Item name is required')

    return errors

  def createItem(self, form_data, user):
    item = Item.objects.create(
      name = form_data['name'],
    )


class Item(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()
