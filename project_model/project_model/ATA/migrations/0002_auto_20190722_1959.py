# Generated by Django 2.2.3 on 2019-07-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matapelajaran',
            name='jadwal_berakhir',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='matapelajaran',
            name='jadwal_dimulai',
            field=models.TimeField(),
        ),
    ]