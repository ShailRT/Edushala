# Generated by Django 4.0.4 on 2022-06-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0027_coursemodel_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='eligibilty',
            field=models.TextField(blank=True, null=True),
        ),
    ]