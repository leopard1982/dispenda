# Generated by Django 5.0.6 on 2024-07-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0037_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='c2d2da72-2b5e-435a-8010-50a8f7b40348', max_length=36, primary_key=True, serialize=False),
        ),
    ]
