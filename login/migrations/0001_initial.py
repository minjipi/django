# Generated by Django 3.1 on 2020-08-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postnum', models.IntegerField()),
                ('posttitle', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=50)),
                ('createdtime', models.DateTimeField()),
                ('nowtime', models.TimeField()),
            ],
        ),

    ]
