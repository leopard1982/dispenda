# Generated by Django 5.0.7 on 2024-07-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0028_alter_bab2_data_umum_id_data_umum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bab3_pap',
            name='is_obj',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='9d1e4f08-f4d4-48e3-b588-8f5641f0fd84', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='717a022b-ec7e-439d-92bb-68ca8e3dc187', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='612181bf-e597-4862-9722-5c3ff2f96807', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='f33714b6-1b20-4c61-a542-19eb2265948a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='6aaa1b3a-579e-4195-a41b-66d9a2f443af', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='a3177b9b-747c-4f59-a10b-cb2cc5cdea13', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='ac3057c8-b546-4019-a11a-c8904d91135c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='556ed44d-f49c-4aa9-8711-f2cfde908619', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='776e1dcd-7b9c-46d7-8787-dfb6ea2bc84e', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='aabcf9c4-fdac-422e-b95b-aff28afc9a5a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='62241638-70d3-49e5-9cc4-20e361976a06', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb',
            name='id_bbnkb',
            field=models.CharField(default='38f30afa-4265-478f-b7e2-24f492f50214', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb_detail',
            name='id_bbnkb_detail',
            field=models.CharField(default='5d5d8304-8a60-49bd-835d-bee05ac39082', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap',
            name='id_pap',
            field=models.CharField(default='8bda6f02-955f-494f-9150-8f653f8f5d45', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun1',
            name='id_pap_tahun1',
            field=models.CharField(default='336d4de0-458f-41fd-afb5-b9dc71346e65', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun2',
            name='id_pap_tahun2',
            field=models.CharField(default='7da77961-98d1-416a-9d68-50b349ab040a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='d2b19571-695c-4947-b896-07a1dd0e3b40', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='6f883b2c-39b6-4adf-a9b6-bd4f301004f2', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='5ec1f64e-b973-4c9a-bf60-65d8f4fc7284', max_length=36, primary_key=True, serialize=False),
        ),
    ]
