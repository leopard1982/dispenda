# Generated by Django 5.0.6 on 2024-06-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0002_alter_trxlhe_id_lhe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxlhe',
            name='id_lhe',
            field=models.CharField(default='e5bcfdcb-d3cf-46ed-939f-5f0a7bf3f3a6', max_length=36, primary_key=True, serialize=False),
        ),
    ]