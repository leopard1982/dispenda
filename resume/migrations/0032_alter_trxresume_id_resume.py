# Generated by Django 5.0.6 on 2024-06-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0031_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='f3a54616-a4f2-4851-ba2d-c4735279cc80', max_length=36, primary_key=True, serialize=False),
        ),
    ]
