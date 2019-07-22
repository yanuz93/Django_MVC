from django.contrib import admin
from .models import Mentee, Mentor, Direksi, MataPelajaran, Challenge, LiveCode

# Register your models here.
@admin.register(Mentee)
class AuthorMentee(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'nomor_telepon')
    list_display_links = ('id', 'nama_lengkap')
    search_fields = ['nama_lengkap']

@admin.register(Mentor)
class AuthorMentor(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'nomor_telepon')
    list_display_links = ('id', 'nama_lengkap')
    search_fields = ['nama_lengkap']

@admin.register(Direksi)
class AuthorDireksi(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'jabatan')
    list_display_links = ('id', 'nama_lengkap')
    search_fields = ['nama_lengkap']

@admin.register(MataPelajaran)
class AuthorMapel(admin.ModelAdmin):
    list_display = ('id', 'nama_pelajaran', 'jadwal_dimulai')
    list_display_links = ('id', 'nama_pelajaran')
    search_fields = ['nama_pelajaran']

@admin.register(Challenge)
class AuthorClg(admin.ModelAdmin):
    list_display = ('id', 'nama_challenge', 'banyak_soal')
    list_display_links = ('id', 'nama_challenge')
    search_fields = ['nama_challenge']

@admin.register(LiveCode)
class AuthorLC(admin.ModelAdmin):
    list_display = ('id', 'nama_live_code', 'banyak_soal')
    list_display_links = ('id', 'nama_live_code')
    search_fields = ['nama_live_code']
