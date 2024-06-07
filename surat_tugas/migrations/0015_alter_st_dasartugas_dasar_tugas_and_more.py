# Generated by Django 5.0.6 on 2024-06-07 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tugas', '0014_alter_st_dasartugas_dasar_tugas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='st_dasartugas',
            name='dasar_tugas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat_tugas.masterdasarst'),
        ),
        migrations.AlterField(
            model_name='st_peserta',
            name='id_surat',
            field=models.CharField(max_length=50),
        ),
    ]