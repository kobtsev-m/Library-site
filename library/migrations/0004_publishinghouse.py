# Generated by Django 2.2.6 on 2020-10-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20201018_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('foundation_year', models.SmallIntegerField()),
                ('country', models.CharField(max_length=2)),
            ],
        ),
    ]