# Generated by Django 5.0.6 on 2024-06-13 19:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0011_alter_headerlhe_id_lhe_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='simpulanhasilvalbin',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='headerlhe',
            name='id_lhe',
            field=models.CharField(default='9cc227dd-a349-401b-89d4-6952996d3e32', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kepegawaianlhe',
            name='id_kepegawaian',
            field=models.CharField(default='<function uuid4 at 0x0000019243199120>', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default=uuid.UUID('43575289-147d-4da3-835a-f51001b65aad'), max_length=36, primary_key=True, serialize=False),
        ),
    ]
