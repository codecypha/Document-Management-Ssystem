# Generated by Django 3.1.4 on 2021-04-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0007_auto_20210409_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='retention',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Always Available', 'Always Available')], default='Inactive', max_length=20),
        ),
    ]
