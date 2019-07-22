from django.contrib import admin
from .models import Resep, Dokter, Pasien, Obat
 

# Register your models here.
@admin.register(Resep)
class AuthorResep(admin.ModelAdmin):
    list_display = ('id', 'nama', 'kumpulan_obat')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Dokter)
class AuthorDokter(admin.ModelAdmin):
    list_display = ('id', 'nama', 'nomor_telepon')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Pasien)
class AuthorPasien(admin.ModelAdmin):
    list_display = ('id', 'nama', 'keluhan')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

@admin.register(Obat)
class Author(admin.ModelAdmin):
    list_display = ('id', 'nama', 'khasiat')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

