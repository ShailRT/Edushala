# Generated by Django 4.0.6 on 2022-07-11 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0029_collegemodel_rank_collegemodel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbroadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('overview', models.TextField(blank=True, null=True)),
                ('admission', models.TextField(blank=True, null=True)),
                ('eligibilty', models.TextField(blank=True, null=True)),
                ('entrance', models.TextField(blank=True, null=True)),
                ('fees', models.TextField(blank=True, null=True)),
                ('fees_table', models.TextField(blank=True, null=True)),
                ('colleges', models.TextField(blank=True, null=True)),
                ('salary', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.AlterField(
            model_name='collegemodel',
            name='rank',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
