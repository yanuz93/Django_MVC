# Generated by Django 2.2.3 on 2019-07-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('spesies', models.CharField(max_length=50)),
                ('berat', models.PositiveIntegerField(max_length=10)),
                ('umur', models.PositiveIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('isi_kandang', models.TextField(max_length=500)),
                ('luas_kandang', models.PositiveIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nomor_telepon', models.CharField(max_length=17)),
                ('hari_berkunjung', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nomor_telepon', models.CharField(max_length=17)),
                ('jadwal_jaga', models.DateField(max_length=20)),
            ],
        ),
    ]