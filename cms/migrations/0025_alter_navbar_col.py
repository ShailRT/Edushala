# Generated by Django 4.0.4 on 2022-06-24 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_navbar_cr_alter_navbar_col'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='col',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.collegemodel'),
        ),
    ]
