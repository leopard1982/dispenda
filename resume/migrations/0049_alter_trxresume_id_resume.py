# Generated by Django 5.0.6 on 2024-07-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0048_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='3b031bfd-7c33-4b5a-9d94-da59f848482a', max_length=36, primary_key=True, serialize=False),
        ),
    ]