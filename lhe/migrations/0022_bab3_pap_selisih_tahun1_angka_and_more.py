# Generated by Django 5.0.6 on 2024-07-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0021_bab3_pap_tahun1_tahun_bab3_pap_tahun2_tahun_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bab3_pap',
            name='selisih_tahun1_angka',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pap',
            name='selisih_tahun1_persen',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pap',
            name='selisih_tahun2_angka',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pap',
            name='selisih_tahun2_persen',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='f9b62e08-afdd-4740-9159-d39fabb9f2a5', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='37aaebf3-0ce4-4c11-9659-e18a8034023e', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='24f07b34-5d67-4284-aa2c-bee95ac94fcb', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='c8451609-9c6b-458b-93d6-26eb09df60b0', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='5efafda4-e73f-4056-8e12-c6f8edaad5d5', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='20dda699-e522-49ed-aefa-5836ff2b1a77', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='33a17d44-9e4a-4e27-85b5-0fdaefbb2fe4', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='69c0912b-62f3-4d77-978f-adc1866edd55', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='1151139c-2da1-42c1-b326-8552eef9917b', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='0e1a688b-ea53-467f-9ee5-2e6e4967a851', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='a270dda8-25c4-4348-a59a-1acc32719dfd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb',
            name='id_bbnkb',
            field=models.CharField(default='a25ec512-89ad-4f62-802e-c27b951c6da6', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb_detail',
            name='id_bbnkb_detail',
            field=models.CharField(default='b256215f-7edb-4630-bf30-e63e587b90b4', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap',
            name='id_pap',
            field=models.CharField(default='794e69ae-9497-49a6-b134-85813c70b011', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun1',
            name='id_pap_tahun1',
            field=models.CharField(default='8092542c-aa9c-42ad-91de-82a3d15168ee', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun2',
            name='id_pap_tahun2',
            field=models.CharField(default='7d4b59e2-4102-4335-a010-2ea0cc75a277', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='1f0965ff-0385-49bc-acc4-4f55023de8e2', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='d4838b7b-9445-420d-888c-20b083c40da9', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='30c0d445-218e-408f-883f-f362e6163b7f', max_length=36, primary_key=True, serialize=False),
        ),
    ]
