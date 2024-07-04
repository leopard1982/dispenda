# Generated by Django 5.0.6 on 2024-07-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0007_bab3_pkb_is_periode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bab3_pkb',
            name='obj_data_piutang',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='obj_data_piutang_nominal',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='obj_pelunasan_piutang',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='obj_pelunasan_piutang_persen',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='pelunasan_piutang_persen',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='pelunasan_piutang_rupiah',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='ab89647f-43b2-43e0-a852-7ca5fff27815', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='ffa22398-c225-43c6-88b6-10bfe813dbb8', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='42a64c41-1d83-4610-8655-3bf0e493b075', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='6e491322-3453-4590-bafa-e79e8a3b221a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='5e0184d6-ab8f-430b-b6a7-40e69ae092df', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='d901ef41-fac4-431d-8fcf-7159acff7feb', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='0d3deff6-2eb2-425d-986d-59f4b76fe081', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='44e8d6c7-fff5-4e1e-8fb1-1ac508d3c62c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='54e96165-0b69-411c-8d48-3a3e65895e51', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='90978307-306a-456b-8aaa-daa4ce5a904e', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='d32c9813-b268-47d3-8a63-db056cf019d0', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='780fdf15-b5ad-4873-8c62-21c804346b4a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='tahun_awal',
            field=models.PositiveSmallIntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='5e43b1b3-f514-4d62-a1d8-a1612edbf0a1', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='068ba0f5-e13e-43a0-b513-2c7e88ad69dc', max_length=36, primary_key=True, serialize=False),
        ),
    ]