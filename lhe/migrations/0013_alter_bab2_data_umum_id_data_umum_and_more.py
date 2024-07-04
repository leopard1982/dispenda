# Generated by Django 5.0.6 on 2024-07-03 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0012_bab3_pkb_jml_pkb_hitam_bab3_pkb_jml_pkb_kuning_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='71fbf244-9e6d-4701-ab2e-67b44d3bef17', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='1a54389f-1992-4fc1-aa6b-31cd53026937', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='88f143c9-ec0f-4137-9f90-ade854f925c7', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='9c5ff425-45a3-429f-b881-70b2c5594da1', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='5c681696-8661-4924-b293-5b1b7c5b9a0d', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='e7b6845c-a818-4f78-a0a3-881c11271d07', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='a90e255c-2f2c-46c9-98ba-693c08d81285', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='b4b7a83a-caff-4173-b66a-09e0d59a1861', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='3c094aad-22f3-4682-bec8-56a51a610196', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='00f66ecd-c7b0-4abf-a07a-5903b7476659', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='f5daea78-7456-4536-a032-c6dd5b27faf7', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='b176a58e-96e8-464a-88f8-24765ee4b377', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='1f5b5439-72cc-483a-a63c-c25d520daf9a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='7d072686-8e0a-429b-8347-a7431da6a54b', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='bab3_bbnkb',
            fields=[
                ('id_bbnkb', models.CharField(default='af3b703d-f565-40c1-a842-adba19b2eebe', max_length=36, primary_key=True, serialize=False, unique=True)),
                ('bulan_awal', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=1)),
                ('bulan_akhir', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=12)),
                ('tahun_awal', models.PositiveSmallIntegerField(default=2023)),
                ('tahun_akhir', models.PositiveSmallIntegerField(default=2024)),
                ('uppd', models.CharField(blank=True, max_length=100, null=True)),
                ('keterangan', models.CharField(max_length=200)),
                ('selisih_angka', models.BigIntegerField(blank=True, default=0, null=True)),
                ('selisih_persen', models.FloatField(blank=True, default=0.0, null=True)),
                ('createdBy', models.CharField(default='', max_length=50)),
                ('createdAt', models.CharField(default='', max_length=50)),
                ('is_periode', models.BooleanField(blank=True, null=True)),
                ('obj_data_piutang', models.IntegerField(blank=True, default=0, null=True)),
                ('obj_data_piutang_nominal', models.BigIntegerField(blank=True, default=0, null=True)),
                ('obj_pelunasan_piutang', models.IntegerField(blank=True, default=0, null=True)),
                ('obj_pelunasan_piutang_persen', models.FloatField(blank=True, default=0, null=True)),
                ('pelunasan_piutang_rupiah', models.BigIntegerField(blank=True, default=0, null=True)),
                ('pelunasan_piutang_persen', models.FloatField(blank=True, default=0, null=True)),
                ('is_new', models.BooleanField(blank=True, null=True)),
                ('jml_pkb_roda4', models.IntegerField(blank=True, default=0, null=True)),
                ('jml_pkb_kuning', models.IntegerField(blank=True, default=0, null=True)),
                ('jml_pkb_hitam', models.IntegerField(blank=True, default=0, null=True)),
                ('penelitian_ulang', models.IntegerField(blank=True, default=0, null=True)),
                ('id_lhe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='lhe.headerlhe')),
            ],
        ),
        migrations.CreateModel(
            name='bab3_bbnkb_detail',
            fields=[
                ('id_pkb_detail', models.CharField(default='1698bce4-66aa-4925-a706-db5e520e452d', max_length=36, primary_key=True, serialize=False)),
                ('bulan', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=1)),
                ('tahun_awal', models.PositiveSmallIntegerField(default=2024)),
                ('tahun_akhir', models.PositiveSmallIntegerField(default=2024)),
                ('nilai_awal', models.BigIntegerField(default=0)),
                ('nilai_akhir', models.BigIntegerField(default=0)),
                ('selisih_angka', models.BigIntegerField(blank=True, default=0, null=True)),
                ('selisih_persen', models.FloatField(blank=True, default=0.0, null=True)),
                ('createdBy', models.CharField(default='', max_length=50)),
                ('createdAt', models.CharField(default='', max_length=50)),
                ('id_pkb', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='lhe.bab3_pkb')),
            ],
        ),
    ]