# Generated by Django 3.2.9 on 2021-11-21 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0026_auto_20211121_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddUserDept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=120)),
                ('entry_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
