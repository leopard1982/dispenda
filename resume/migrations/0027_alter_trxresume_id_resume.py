# Generated by Django 5.0.6 on 2024-06-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0026_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='21765988-5be9-47f6-aaaf-099c36b86a1e', max_length=36, primary_key=True, serialize=False),
        ),
    ]
