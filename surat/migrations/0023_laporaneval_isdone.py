# Generated by Django 4.2.7 on 2023-12-26 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0022_alter_laporaneval_nomor_surat_tugas'),
    ]

    operations = [
        migrations.AddField(
            model_name='laporaneval',
            name='isDone',
            field=models.BooleanField(default=False, verbose_name='Laporan Evaluasi Selesai'),
        ),
    ]
