# Generated by Django 5.0.7 on 2024-07-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0058_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='e2633df7-04cb-4ed2-beca-f3ac44495e2a', max_length=36, primary_key=True, serialize=False),
        ),
    ]
