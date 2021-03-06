# Generated by Django 3.0.4 on 2020-03-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField()),
                ('admit_date', models.DateTimeField(auto_now=True)),
                ('discharge_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
