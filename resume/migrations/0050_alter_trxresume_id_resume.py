# Generated by Django 5.0.6 on 2024-07-10 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0049_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='5471a58d-bd84-4294-9fdf-5b19280656ba', max_length=36, primary_key=True, serialize=False),
        ),
    ]