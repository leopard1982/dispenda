# Generated by Django 5.0.6 on 2024-06-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0007_alter_headerlhe_id_lhe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerlhe',
            name='id_lhe',
            field=models.CharField(default='a76cc1de-3fd7-48e7-9ca1-b4d930b57d6f', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kepegawaianlhe',
            name='id_kepegawaian',
            field=models.CharField(default='<function uuid4 at 0x000002B50DC59120>', max_length=36, primary_key=True, serialize=False),
        ),
    ]