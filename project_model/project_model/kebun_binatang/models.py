from django.db import models
from django.db.models import CharField, DateField, TextField, PositiveIntegerField

# Create your models here.
class Penjaga(models.Model):
    nama = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=17)
    jadwal_jaga = models.DateField(max_length=20)

class Hewan(models.Model):
    nama = models.CharField(max_length=100)
    spesies = models.CharField(max_length=50)
    berat = models.PositiveIntegerField()
    umur = models.PositiveIntegerField()

class Kandang(models.Model):
    nama = models.CharField(max_length=100)
    isi_kandang = models.TextField(max_length=500)
    luas_kandang = models.PositiveIntegerField()
    
class Pengunjung(models.Model):
    nama = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=17)
    hari_berkunjung = models.DateField()

