# Generated by Django 5.0.6 on 2024-07-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0038_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='6fe491bf-874e-4f87-9168-6ee56f23991b', max_length=36, primary_key=True, serialize=False),
        ),
    ]