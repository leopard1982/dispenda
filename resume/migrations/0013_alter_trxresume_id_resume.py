# Generated by Django 5.0.6 on 2024-06-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='28f6cefa-0bb8-4150-9e29-8fed616a3229', max_length=36, primary_key=True, serialize=False),
        ),
    ]
