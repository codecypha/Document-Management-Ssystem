# Generated by Django 3.1.4 on 2021-04-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0009_auto_20210409_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvals',
            name='status',
            field=models.CharField(default='Pencing', max_length=10),
        ),
    ]
