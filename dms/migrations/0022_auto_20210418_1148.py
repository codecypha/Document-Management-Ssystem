# Generated by Django 3.1.4 on 2021-04-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0021_auto_20210418_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]