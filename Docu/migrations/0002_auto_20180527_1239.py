# Generated by Django 2.0.5 on 2018-05-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='subpagina',
            field=models.ManyToManyField(blank=True, to='Docu.Pagina'),
        ),
    ]
