# Generated by Django 5.0.6 on 2024-07-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0017_alter_bab2_data_umum_id_data_umum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='cbc076a9-8ca1-4365-b72e-6f5dc0a818f5', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='42e79aa5-cf8c-4a20-ac78-dd8571c0c56c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='2ec34cd0-f6c1-48dc-b806-07178ad63525', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='4306893d-89f2-42a0-b616-f5f1f53c7ef3', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='0528d9d8-a775-4ea9-9eb1-80315248c2ac', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='32106480-b205-4422-8b7d-da36c7db970a', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='2fd918c5-9c1e-4669-aacc-2aa59148a037', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='8c38e778-74c9-409e-9692-6710106aabfd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='72c696d0-91a1-4f74-bb26-ee476d85ff19', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='3ec2e287-d096-4360-a0b4-1a33a06904bd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='dfba89ab-70c4-4a70-ac90-23216523f94b', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb',
            name='id_bbnkb',
            field=models.CharField(default='392f5f68-0c46-4b6e-9552-cb0abda71765', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb_detail',
            name='id_bbnkb_detail',
            field=models.CharField(default='29f72929-c7ef-4405-81f4-0a3af122a780', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='48ac6142-84d7-40da-a168-1b1cede4ebc0', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='3b4884b9-25f0-4bb0-9b03-87e43e654982', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='7d265964-b952-4cd5-ab30-68c64f9d9164', max_length=36, primary_key=True, serialize=False),
        ),
    ]
