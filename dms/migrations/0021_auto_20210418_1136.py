# Generated by Django 3.1.4 on 2021-04-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0020_auto_20210417_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='country',
            field=models.CharField(default='Nigeria', max_length=25),
        ),
    ]