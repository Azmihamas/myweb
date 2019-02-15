# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    nama = "Azmi"
    buah = ['apel','anggur','semangka']
    return render(request,'index.html'), {'nama':nama, 'buah':buah}

def about(request):
    return render(request,'about.html')
    
def kontak(request):
    return render(request,'kontak.html')

def blog(request):
    return render(request,'blog.html')  

def menu(request):
    return render(request,'menu.html')
