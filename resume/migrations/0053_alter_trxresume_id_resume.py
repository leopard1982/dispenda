# Generated by Django 5.0.7 on 2024-07-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0052_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='bc7fc0c4-454b-4353-a4bf-d691df3eac80', max_length=36, primary_key=True, serialize=False),
        ),
    ]
