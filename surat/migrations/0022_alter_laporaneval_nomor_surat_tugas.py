# Generated by Django 4.2.7 on 2023-12-26 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0021_alter_laporaneval_periode_akhir_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporaneval',
            name='Nomor_Surat_Tugas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.surattugas', verbose_name='Nomor Acuan Surat Tugas'),
        ),
    ]
