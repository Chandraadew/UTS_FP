
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk,tambah_barang, Barang_View, member, jenis

def coba1(request):
    return HttpResponse('Selamat Pagi Kawan....')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2, name = "index"),
    path('produk/',produk, name = "produk"),
    path('addbrg/',tambah_barang),
    path('Vbrg/',Barang_View, name = "Vbrg"),
    path('member/',member, name = "member"),
    path('jenis/',jenis, name= "jenis")
]
