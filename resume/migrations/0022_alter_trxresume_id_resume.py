# Generated by Django 5.0.6 on 2024-06-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0021_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='e4e4a11f-23cc-46cc-b8f2-d8281554e850', max_length=36, primary_key=True, serialize=False),
        ),
    ]