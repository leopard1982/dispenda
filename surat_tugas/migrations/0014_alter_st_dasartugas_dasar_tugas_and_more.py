# Generated by Django 5.0.6 on 2024-06-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tugas', '0013_alter_st_dasartugas_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='st_dasartugas',
            name='dasar_tugas',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='st_dasartugas',
            name='id_surat',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='st_dasartugas',
            unique_together={('id_surat', 'dasar_tugas')},
        ),
    ]
