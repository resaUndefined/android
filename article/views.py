# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def Myview(request):
	return HttpResponse('<h1>halooo ini halaman pertama')

def Hello_world(request):
	return HttpResponse('Hello world')

def NamaSaya(request,nama_saya,umur):
	return HttpResponse('<marquee behavior="alternate" direction="down">Hello nama saya adalah %s, umur saya adalah %s tahun</marquee>' % (nama_saya,umur))

def Coba(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def Home(request):
	return render(request, 'index.html')

