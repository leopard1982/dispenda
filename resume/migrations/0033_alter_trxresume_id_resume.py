# Generated by Django 5.0.6 on 2024-06-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0032_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='f975bd86-924a-4515-93cf-00601a1031be', max_length=36, primary_key=True, serialize=False),
        ),
    ]