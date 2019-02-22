from __future__ import unicode_literals
from django.shortcuts import render
from.models import Artikel

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
    #selact * from Artikel
    blogs = Artikel.objects.all()
    return render(request,'layout/blog.html',{'blogs':blogs})  

def menu(request):
    return render(request,'menu.html')
