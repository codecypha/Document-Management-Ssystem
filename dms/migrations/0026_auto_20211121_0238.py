# Generated by Django 3.2.9 on 2021-11-21 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0025_folder_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='addusergroup',
            name='group_name',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addusergroup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='approvals',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department',
            name='group_name',
            field=models.CharField(blank=True, max_length=125),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='filetype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='groupmanagement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='versionupload',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]