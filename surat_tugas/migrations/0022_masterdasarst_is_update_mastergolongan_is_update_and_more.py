# Generated by Django 5.0.7 on 2024-07-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat_tugas', '0021_remove_masterdasarst_is_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterdasarst',
            name='is_update',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='mastergolongan',
            name='is_update',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='masterjabatan',
            name='is_update',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]