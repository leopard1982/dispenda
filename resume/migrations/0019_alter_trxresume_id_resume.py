# Generated by Django 5.0.6 on 2024-06-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_alter_trxresume_id_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trxresume',
            name='id_resume',
            field=models.CharField(default='636d24d7-37a6-4c2f-91aa-5e344f3669a2', max_length=36, primary_key=True, serialize=False),
        ),
    ]