# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .models import *

def index(request):
  items = Item.objects.all()

  context = {
    'Item': items,
  }

  return render(request, 'wish_list/dashboard.html', context)

def createPage(request):
    return render(request, 'wish_list/create_page.html')

def create(request):
  if request.method == 'POST':
    errors = Item.objects.validate(request.POST)
    print errors

    if not errors:
      current_user = User.objects.currentUser(request)
      item = Item.objects.createItem(request.POST, current_user)

      return redirect('/dashboard')
  return redirect(reverse('wish-page'))




 # def delete(request, id):
 #
