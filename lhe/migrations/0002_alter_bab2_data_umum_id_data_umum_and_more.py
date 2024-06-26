# Generated by Django 5.0.6 on 2024-06-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='e1f6caf1-2ff3-4c8b-b499-666e8839cb1c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='cfb3c161-5d85-4934-9cda-a13ce9c0637d', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='18b84fac-2486-4d86-be48-19c39747c415', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='8d04c036-6dae-4f69-b7ca-de8da5ddb8eb', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='42248f9e-f2bf-4af4-add1-10e531618b7d', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='4697e848-979f-41a8-977d-0ac120ea8609', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='71f7dd9f-6142-4933-8326-46aad3cc7043', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='9c2cccb2-7a4c-4297-a4dd-1341d285daee', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='218e27cb-c361-4564-80cd-5820b13fabba', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='8259927d-9b37-456d-8ca7-19cab88e1b5f', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='d21b0bad-e3b4-447a-aecf-be65e8b8a52e', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='3235c5aa-1206-4fd5-a6f2-8bc1dba40d18', max_length=36, primary_key=True, serialize=False),
        ),
    ]
