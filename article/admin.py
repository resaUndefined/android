# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Category,Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
