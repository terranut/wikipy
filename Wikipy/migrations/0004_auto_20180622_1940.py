# Generated by Django 2.0.6 on 2018-06-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wikipy', '0003_auto_20180622_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
