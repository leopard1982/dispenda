# Generated by Django 5.0.6 on 2024-06-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='06497746-d092-4c45-87f8-7a8bbb43a1a0', max_length=36, primary_key=True, serialize=False),
        ),
    ]
