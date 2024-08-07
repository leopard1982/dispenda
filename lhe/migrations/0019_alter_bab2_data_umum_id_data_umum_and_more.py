# Generated by Django 5.0.6 on 2024-07-07 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0018_alter_bab2_data_umum_id_data_umum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='b893c456-eeb6-4abb-ba5d-17507910ef65', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='97ee295c-8e90-4811-948a-3502b5494752', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='e5db8f84-3cd4-4964-ab25-6be1d75afacb', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='11e2b877-6bf4-49a1-9a2a-9a612f21b8c0', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='da6d9dda-ddd8-4f85-bc3f-31219db5fd5c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='27b89762-74c0-40f9-9028-2a8854e14840', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='cd16adb6-4853-423a-81ef-4256e407b562', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='476a853b-5212-409b-aa65-fca5861e9d64', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='857a7270-e534-488f-887a-b7ff5b163855', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='e013e48a-5766-462c-9248-b02f8a6bb084', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='ef8aabac-8c9e-476d-968c-e59fd19a8337', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb',
            name='id_bbnkb',
            field=models.CharField(default='05c598fb-9485-43fa-87ab-5c47fc9b1c0d', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb_detail',
            name='id_bbnkb_detail',
            field=models.CharField(default='7ec9f134-1e44-4622-9b5c-18f7636aece5', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='f7cbc1af-4606-4a23-858a-518a269fbb80', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='4a4c7bf2-56f3-435f-9fe4-45a05fbdef7d', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='13bd2634-e112-423a-8564-1f9362f0bf0f', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='bab3_pap',
            fields=[
                ('id_pap', models.CharField(default='d0ae87df-1559-4a8f-85db-967c386553ae', max_length=36, primary_key=True, serialize=False, unique=True)),
                ('bulan1_awal', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=1)),
                ('bulan1_akhir', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=12)),
                ('bulan2_awal', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=1)),
                ('bulan2_akhir', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=12)),
                ('tahun1', models.PositiveSmallIntegerField(default=2023)),
                ('tahun2', models.PositiveSmallIntegerField(default=2024)),
                ('is_new', models.BooleanField(blank=True, default=False, null=True)),
                ('createdAt', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=100, null=True)),
                ('id_lhe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='lhe.headerlhe')),
            ],
        ),
        migrations.CreateModel(
            name='bab3_pap_tahun1',
            fields=[
                ('id_pap_tahun1', models.CharField(default='9ced9abc-5220-471a-b615-18c57b8a4e61', max_length=36, primary_key=True, serialize=False)),
                ('bulan', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=1)),
                ('penetapan', models.BigIntegerField(default=0)),
                ('pembayaran', models.BigIntegerField(default=0)),
                ('selisih_angka', models.BigIntegerField(blank=True, default=0, null=True)),
                ('selisih_persen', models.FloatField(blank=True, default=0, null=True)),
                ('createdAt', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=100, null=True)),
                ('id_pap', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='lhe.bab3_pap')),
            ],
        ),
        migrations.CreateModel(
            name='bab3_pap_tahun2',
            fields=[
                ('id_pap_tahun2', models.CharField(default='004b0b8e-a597-4023-9a38-82877d48fc20', max_length=36, primary_key=True, serialize=False)),
                ('bulan', models.PositiveSmallIntegerField(choices=[(1, 'JANUARI'), (2, 'FEBRUARI'), (3, 'MARET'), (4, 'APRIL'), (5, 'MEI'), (6, 'JUNI'), (7, 'JULI'), (8, 'AGUSTUS'), (9, 'SEPTEMBER'), (10, 'OKTOBER'), (11, 'NOVEMBER'), (12, 'DESEMBER')], default=1)),
                ('penetapan', models.BigIntegerField(default=0)),
                ('pembayaran', models.BigIntegerField(default=0)),
                ('selisih_angka', models.BigIntegerField(blank=True, default=0, null=True)),
                ('selisih_persen', models.FloatField(blank=True, default=0, null=True)),
                ('createdAt', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=100, null=True)),
                ('id_pap', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='lhe.bab3_pap')),
            ],
        ),
    ]
