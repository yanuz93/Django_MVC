# Generated by Django 2.2.3 on 2019-07-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=25)),
                ('nomor_telepon', models.CharField(max_length=17)),
                ('bidang', models.CharField(max_length=10)),
                ('jadwal_praktek', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=10)),
                ('kandungan', models.CharField(max_length=25)),
                ('khasiat', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=10)),
                ('nomor_telepon', models.CharField(max_length=17)),
                ('alamat', models.TextField(max_length=40)),
                ('keluhan', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=10)),
                ('total_harga', models.PositiveIntegerField(max_length=9)),
                ('kumpulan_obat', models.TextField(max_length=10)),
            ],
        ),
    ]
