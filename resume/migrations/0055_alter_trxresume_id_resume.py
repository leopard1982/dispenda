# Generated by Django 5.0.7 on 2024-07-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0054_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='0909f592-c119-437b-92d8-d7df4834b443', max_length=36, primary_key=True, serialize=False),
        ),
    ]
