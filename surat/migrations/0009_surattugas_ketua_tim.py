# Generated by Django 4.2.7 on 2023-12-18 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0008_alter_surattugas_tanggal_surat'),
    ]

    operations = [
        migrations.AddField(
            model_name='surattugas',
            name='Ketua_Tim',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='surat.pegawai'),
            preserve_default=False,
        ),
    ]
