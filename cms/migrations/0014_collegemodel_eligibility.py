# Generated by Django 4.0.4 on 2022-06-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_collegemodel_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegemodel',
            name='eligibility',
            field=models.TextField(blank=True, null=True),
        ),
    ]