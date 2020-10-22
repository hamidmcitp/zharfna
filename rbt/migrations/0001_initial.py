# Generated by Django 3.1.2 on 2020-10-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OwnerName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='RbtMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RbtName', models.CharField(max_length=40)),
                ('RbtSinger', models.CharField(max_length=40)),
                ('RbtCode', models.IntegerField(max_length=10)),
                ('RbtOwner', models.CharField(max_length=40)),
                ('RbtCost', models.IntegerField(max_length=4)),
                ('RbtDescription', models.CharField(max_length=100)),
                ('RbtDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SingerName', models.CharField(max_length=40)),
                ('SingerBirthDay', models.DateField()),
            ],
        ),
    ]
