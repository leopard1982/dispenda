# Generated by Django 5.0.6 on 2024-07-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0016_alter_bab2_data_umum_id_data_umum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='862d7397-d417-4592-a35f-04632c44f29a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='5260f83d-cf2f-4e51-a698-e6527052742d', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='3f53237f-f0b7-4f9e-b183-7d5d578b76cd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='762fd189-a836-4cd9-a854-1f64eb6c4d30', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='7683e750-b5f3-4633-8adb-ffdf0786bbc9', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='70c9e6c1-3ba0-41de-ad1d-1070d5d3ce10', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='8c44c1c9-29ef-4ba8-93d7-dc1bc96af3a3', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='7a64dd15-26de-46f1-bf6e-9963c603a1f5', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='5c454e91-d13d-4c60-b986-975533c85784', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='e0d95329-fcbf-4f74-8108-300b2a6024be', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='76308d70-652f-4544-be41-3363d39c0d58', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb',
            name='id_bbnkb',
            field=models.CharField(default='be91ef60-de84-48a3-a51f-cce7d2eb2669', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb_detail',
            name='id_bbnkb_detail',
            field=models.CharField(default='2a3ea168-4c93-4157-824e-8c7f4266e7c8', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='e203d773-9812-4765-b078-05596eecad19', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='6f12c6a4-ad74-4c09-9426-b35f2e50c7b8', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='d7f088ff-7076-432c-b288-50fbb9c0bf58', max_length=36, primary_key=True, serialize=False),
        ),
    ]
