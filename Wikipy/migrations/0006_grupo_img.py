# Generated by Django 2.0.6 on 2018-06-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wikipy', '0005_auto_20180623_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
