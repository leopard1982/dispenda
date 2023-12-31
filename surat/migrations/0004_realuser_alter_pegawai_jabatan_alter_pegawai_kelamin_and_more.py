# Generated by Django 4.2.7 on 2023-12-15 00:51

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('surat', '0003_jabatan_pegawai'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('isCreate', models.BooleanField(default=False)),
                ('isList', models.BooleanField(default=True)),
                ('isUpdate', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='pegawai',
            name='Jabatan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.jabatan', verbose_name='Jabatan*'),
        ),
        migrations.AlterField(
            model_name='pegawai',
            name='Kelamin',
            field=models.CharField(choices=[('P', 'Pria'), ('W', 'Wanita')], max_length=1, verbose_name='Jenis Kelamin*'),
        ),
        migrations.AlterField(
            model_name='pegawai',
            name='NIP',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Nomor Induk Pegawai*'),
        ),
        migrations.AlterField(
            model_name='pegawai',
            name='Nama',
            field=models.CharField(max_length=50, verbose_name='Nama Pegawai*'),
        ),
    ]
