# Generated by Django 3.0.4 on 2020-04-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200414_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[('1', 'doctor'), ('2', 'patient')], default=False),
        ),
    ]
