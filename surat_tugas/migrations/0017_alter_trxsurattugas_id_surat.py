# Generated by Django 5.0.6 on 2024-06-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tugas', '0016_trxsurattugas_is_lhe_trxsurattugas_is_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxsurattugas',
            name='id_surat',
            field=models.CharField(default='', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
    ]
