# Generated by Django 5.0.7 on 2024-07-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0059_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='4e532b0c-fc62-44e8-be09-e8b431184f1e', max_length=36, primary_key=True, serialize=False),
        ),
    ]
