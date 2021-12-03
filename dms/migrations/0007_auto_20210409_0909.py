# Generated by Django 3.1.4 on 2021-04-09 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0006_auto_20210408_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='action',
            field=models.CharField(choices=[('Delete Permently', 'Delete Permently'), ('Set Inactive', 'Set Inactive')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='department',
            name='retention',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Always Available', 'Always Available')], default='Always Available', max_length=20),
        ),
    ]