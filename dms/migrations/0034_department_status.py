# Generated by Django 3.2.9 on 2021-12-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0033_adduserfolder_folder_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='status',
            field=models.CharField(default='active', max_length=220),
        ),
    ]