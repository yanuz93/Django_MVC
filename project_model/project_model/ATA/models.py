from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=17)
    jabatan = models.CharField(max_length=100)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=17)
    nomor_absen = models.SmallIntegerField()
    nilai_rerata = models.FloatField()

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=17)
    matapelajaran_id = models.ForeignKey('MataPelajaran', on_delete=models.CASCADE)

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=100)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=100)
    banyak_soal = models.SmallIntegerField() 
    bobot_nilai = models.SmallIntegerField()
    matapelajaran_id = models.ForeignKey('MataPelajaran', on_delete=models.CASCADE)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=100)
    banyak_soal = models.SmallIntegerField()
    bobot_nilai = models.SmallIntegerField()
    tanggal_pelaksanaan = models.DateField() 
    matapelajaran_id = models.ForeignKey('MataPelajaran', on_delete=models.CASCADE)
