# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from article.models import Category,Post
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

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
	categori = Category.objects.all()
	post = Post.objects.all().order_by('-created_on')[:3]
	#idCate = post.category.id
	data = {
		'categori' : categori,
	#	'idCate' : idCate,
		'post' : post
	}
	return render(request, 'index.html',data)

@login_required(login_url='/login/')
def post_detail(request,slug):
	categori = Category.objects.all()
	posting = Post.objects.get(slug=slug)
	cat = Category.objects.get(name=posting.category)
	data = {
		'categori' : categori,
		'cat' : cat,
		'postDetail' : posting
	}
	return render(request, 'single_post.html',data)

def category_list(request):
	categori = Category.objects.all()
	data = {
			'categori' : categori,
	}
	return render(request,'category.html',data)

def category_detail(request,id):
	categori = Category.objects.get(id=id)
	cateList = Category.objects.all()
	posting = Post.objects.filter(category=categori)
	cate_list = {
		'categori' : cateList,
		'postCate' : posting,
		'cate' : categori
	}
	return render(request,'category_detail.html',cate_list)

def LoginView(request):
	data = {}
	if request.POST:
		username = request.POST.get('uname')
		password = request.POST.get('pass')
		is_auth = authenticate(username=username,password=password)
		if is_auth is not None:
			login(request,is_auth)
			return redirect('/')
		else:
			print "gagal login, silakan cek username dan password anda"
	return render(request,'login.html')


def LogoutView(request):
	logout(request)
	return redirect('/')


