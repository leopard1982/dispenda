# Generated by Django 5.0.6 on 2024-06-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='4038aece-7593-434f-a042-885159b373f9', max_length=36, primary_key=True, serialize=False),
        ),
    ]