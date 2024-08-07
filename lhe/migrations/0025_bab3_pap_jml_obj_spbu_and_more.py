# Generated by Django 5.0.6 on 2024-07-10 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lhe', '0024_bab3_pap_jml_obj_pap_berijin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bab3_pap',
            name='jml_obj_spbu',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bab2_data_umum',
            name='id_data_umum',
            field=models.CharField(default='3d33382d-d9ee-4d07-a412-539659bfdfcd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_sasaran_evaluasi_pembinaan',
            name='id_sasaran',
            field=models.CharField(default='3e64baed-21cf-4cca-9d26-0bcdeb6c66ea', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_bangun_tanah',
            name='id_tu_bagun_tanah',
            field=models.CharField(default='3c3b520f-7e24-4ce8-96d4-155584c04664', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian',
            name='id_tu_kepegawaian',
            field=models.CharField(default='12d4fd19-9994-4a38-af1c-7a9b249f673c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_detail',
            name='id_tu_kepegawaian_detail',
            field=models.CharField(default='cdd78d05-68bf-4fc6-ad08-96c04a4aea0c', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_kepegawaian_normatif',
            name='id_tu_kepegawaian_normatif',
            field=models.CharField(default='9fd53a2b-1a83-4012-98b4-3aaee443b364', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_keuangan',
            name='id_tu_keuangan',
            field=models.CharField(default='3e353202-9f85-450c-9f5d-cc1b4d82fffd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemkab',
            name='id_tu_mobil_pemkab',
            field=models.CharField(default='8bf50e7d-1c86-4f8e-bf42-a01dd19670ad', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_mobil_pemprov',
            name='id_tu_mobil_pemprov',
            field=models.CharField(default='6e4ac370-580a-4fa1-9941-a0346a83a8e7', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tatausaha_motor_pemprov',
            name='id_tu_motor_pemprov',
            field=models.CharField(default='63279b60-6249-4d46-a2b3-85165349cdf9', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab2_tujuan_evaluasi_pembinaan',
            name='id_tujuan',
            field=models.CharField(default='9710df31-9ed1-44f6-86aa-a37f05170cbd', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb',
            name='id_bbnkb',
            field=models.CharField(default='a9ffb78a-5cbe-4875-8e6c-da630b5efcf8', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_bbnkb_detail',
            name='id_bbnkb_detail',
            field=models.CharField(default='631719c9-e67b-49da-b837-325305099d36', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap',
            name='id_pap',
            field=models.CharField(default='61c15bad-abb9-422b-933a-1fd97762769f', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun1',
            name='id_pap_tahun1',
            field=models.CharField(default='71badb1e-a788-46c6-ae07-71b46259c344', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pap_tahun2',
            name='id_pap_tahun2',
            field=models.CharField(default='06f3f569-4bf9-494f-8d98-fd40830c9eb0', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bab3_pkb',
            name='id_pkb',
            field=models.CharField(default='65ee4326-2b97-410a-b620-1b76ca736d00', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bab3_pkb_detail',
            name='id_pkb_detail',
            field=models.CharField(default='bb25725e-3a49-4619-801a-4eb8ddc8fd32', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='simpulanhasilvalbin',
            name='id_simpulan',
            field=models.CharField(default='f952c4ed-9083-47b7-8059-a0a521484f8b', max_length=36, primary_key=True, serialize=False),
        ),
    ]
