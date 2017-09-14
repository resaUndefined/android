# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Category,Post
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','category','created_on','last_modified','image')
	list_filter = ('category','created_on')
	search_fields = ('title','content')
	prepopulated_fields = {'slug' : ('title',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
