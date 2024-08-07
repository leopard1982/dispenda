# Generated by Django 5.0.7 on 2024-07-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0032_alter_bab2_data_umum_id_data_umum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='35896e38-0233-4608-beea-b1475810627e', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='eae710e2-5b32-4b4c-abaf-d4dc0e051caa', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='4c535c77-b7e3-4a59-8a91-990915b4129d', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='170fa01a-7b8b-43ac-a7d2-a9a6b1528931', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='c2129a7e-5d81-407f-a619-b2be8bb481c4', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='1b98435d-c7e8-47f7-90ba-5354721d4573', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='cb8696d9-1327-4f7b-864e-4f3a3a4fa0ba', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='7ba96921-7b3c-4d4a-b7d3-9c19445ca1d3', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='32a3f800-ff31-4289-a273-5020f14f1333', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='d41089c0-dab7-45cd-be17-8be477a2d541', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='d1797cb2-b6b6-4210-9b4c-49e42d291667', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb',
            name='id_bbnkb',
            field=models.CharField(default='8a7d6e0e-f6ff-4c51-9fc6-819e135e4e46', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb_detail',
            name='id_bbnkb_detail',
            field=models.CharField(default='eae7411f-8d15-43ae-87be-c47cfcf5f88c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap',
            name='id_pap',
            field=models.CharField(default='deb52fcc-c2da-49c2-9763-dd49f36de6d3', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun1',
            name='id_pap_tahun1',
            field=models.CharField(default='2fad7449-ffe5-45e5-a9b3-3ef6b7a46552', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun2',
            name='id_pap_tahun2',
            field=models.CharField(default='f59c97b8-faad-443d-b5b4-9dabfa5d1a0f', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='b1f82ba3-fede-4690-99a4-b25825ea3d2d', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='48ce03ff-a8e3-4dbf-9f50-5653d9144398', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='769c5a10-f76e-49b5-85e5-8e88af76d4da', max_length=36, primary_key=True, serialize=False),
        ),
    ]
