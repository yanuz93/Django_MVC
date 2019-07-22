from django.db import models
from django.db.models import CharField, DateField, TextField, PositiveIntegerField

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=17)
    bidang = models.CharField(max_length=50)
    jadwal_praktek = models.DateField(max_length=20)

class Pasien(models.Model):
    nama = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=17)
    alamat = models.TextField(max_length=400)
    keluhan = models.TextField(max_length=1000)

class Resep(models.Model):
    nama = models.CharField(max_length=100)
    total_harga = models.PositiveIntegerField()
    kumpulan_obat = models.TextField(max_length=500)

class Obat(models.Model):
    nama = models.CharField(max_length=100)
    kandungan = models.CharField(max_length=255)
    khasiat = models.TextField(max_length=500)

