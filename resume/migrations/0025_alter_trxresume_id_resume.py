# Generated by Django 5.0.6 on 2024-06-27 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0024_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='fded7aaf-f015-42e6-af26-75218c6ce0e6', max_length=36, primary_key=True, serialize=False),
        ),
    ]