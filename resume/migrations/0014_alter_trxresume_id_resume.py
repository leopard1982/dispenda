# Generated by Django 5.0.6 on 2024-06-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='7dff7752-e5fa-49c8-aedd-075fe080de68', max_length=36, primary_key=True, serialize=False),
        ),
    ]
