# Generated by Django 4.2.7 on 2023-12-15 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0004_realuser_alter_pegawai_jabatan_alter_pegawai_kelamin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DasarSuratTugas',
            fields=[
                ('dasar', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Konfigurasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPLT', models.BooleanField(default=False)),
                ('Kepala_Bapeda', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='surat.pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='ST_Dasar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dasar', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.dasarsurattugas')),
            ],
        ),
        migrations.CreateModel(
            name='ST_Peserta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Struktur',
            fields=[
                ('Kode', models.CharField(default='', max_length=3, primary_key=True, serialize=False, verbose_name='Kode Jabatan')),
                ('Nama_Struktur', models.CharField(max_length=20, verbose_name='Nama Struktur')),
            ],
        ),
        migrations.CreateModel(
            name='SuratTugas',
            fields=[
                ('Nomor_Surat', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('Tanggal_Surat', models.DateField()),
                ('Tugas', models.CharField(max_length=200)),
                ('Lokasi_Tugas', models.CharField(max_length=30)),
                ('Tanggal_Tugas', models.CharField(max_length=30)),
                ('Kepala_Bapeda', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.konfigurasi')),
            ],
        ),
        migrations.DeleteModel(
            name='Coba',
        ),
        migrations.AlterField(
            model_name='jabatan',
            name='Nama_Jabatan',
            field=models.CharField(max_length=20, verbose_name='Nama Jabatan'),
        ),
        migrations.AddField(
            model_name='st_peserta',
            name='Nomor_Surat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.surattugas'),
        ),
        migrations.AddField(
            model_name='st_peserta',
            name='Peserta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.pegawai'),
        ),
        migrations.AddField(
            model_name='st_dasar',
            name='Nomor_Surat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.surattugas'),
        ),
        migrations.AddField(
            model_name='pegawai',
            name='Struktur',
            field=models.ForeignKey(default=" ", on_delete=django.db.models.deletion.RESTRICT, to='surat.struktur', verbose_name='Struktur*'),
            preserve_default=False,
        ),
    ]
