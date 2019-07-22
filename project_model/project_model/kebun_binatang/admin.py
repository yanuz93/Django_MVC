from django.contrib import admin
from .models import Hewan, Penjaga, Pengunjung, Kandang
 

# Register your models here.
@admin.register(Hewan)
class AuthorHewan(admin.ModelAdmin):
    list_display = ('id', 'nama', 'umur')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Penjaga)
class AuthorPenjaga(admin.ModelAdmin):
    list_display = ('id', 'nama', 'nomor_telepon')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Pengunjung)
class AuthorPengunjung(admin.ModelAdmin):
    list_display = ('id', 'nama', 'hari_berkunjung')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Kandang)
class Author(admin.ModelAdmin):
    list_display = ('id', 'nama', 'isi_kandang')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

