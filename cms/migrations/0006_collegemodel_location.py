# Generated by Django 4.0.4 on 2022-06-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_rename_clg_name_collegemodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegemodel',
            name='location',
            field=models.CharField(default='test location', max_length=200),
            preserve_default=False,
        ),
    ]