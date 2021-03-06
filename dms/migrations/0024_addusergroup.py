# Generated by Django 3.1.4 on 2021-04-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0023_department_group_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddUserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=120)),
                ('entry_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
