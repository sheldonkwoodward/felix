# Generated by Django 2.0.1 on 2018-01-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20180101_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('season', models.IntegerField()),
                ('episode', models.IntegerField()),
                ('cut', models.CharField(max_length=250)),
                ('resolution', models.CharField(max_length=250)),
                ('date_added', models.DateTimeField()),
                ('path', models.TextField()),
            ],
        ),
    ]
