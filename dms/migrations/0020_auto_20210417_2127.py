# Generated by Django 3.1.4 on 2021-04-17 20:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0019_auto_20210417_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmanagement',
            name='creator',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupmanagement',
            name='group_name',
            field=models.CharField(max_length=200),
        ),
    ]