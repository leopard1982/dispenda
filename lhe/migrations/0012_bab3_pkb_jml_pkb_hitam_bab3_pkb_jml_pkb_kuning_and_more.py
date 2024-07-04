# Generated by Django 5.0.6 on 2024-07-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0011_bab3_pkb_is_new_alter_bab2_data_umum_id_data_umum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bab3_pkb',
            name='jml_pkb_hitam',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='jml_pkb_kuning',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='jml_pkb_roda4',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='bab3_pkb',
            name='penelitian_ulang',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='e1b630ed-51d0-4b23-a2af-38690843e895', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='c67d1e43-63b5-4cdf-b5ae-585055d8e3ad', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='ac3cc5a7-07dd-493c-9eb8-4974c0ae2937', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='7c9f4a55-7acb-4390-927a-f29942aefe85', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='b246629c-7ae7-47a9-ba4b-956076500b48', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='56e043d1-b071-4168-aeff-a0ec411db513', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='fe84dbad-7bc2-4155-8df7-11980bd40588', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='54a9e158-31ba-4361-8430-1f8c82b41bf8', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='abb227bb-c06d-4deb-bd56-22861a376205', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='1562ff5d-aa76-4fe3-ae43-4aea67bf8d49', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='ec6d4233-76f6-4abd-84da-9788d60515cd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='b7162a84-aaa6-44d4-b313-5b85feeedf41', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='0d0c4ed8-ab83-4c78-be4e-ff43b2d14f53', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='16844828-bcd4-473c-b5a0-f1fb70d48ea9', max_length=36, primary_key=True, serialize=False),
        ),
    ]