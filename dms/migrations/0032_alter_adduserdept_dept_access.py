# Generated by Django 3.2.9 on 2021-11-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0031_adduserdept_dept_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduserdept',
            name='dept_access',
            field=models.CharField(default='full', max_length=5),
        ),
    ]
