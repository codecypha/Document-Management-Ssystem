# Generated by Django 3.1.4 on 2021-04-07 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=220)),
                ('retention', models.CharField(choices=[('Always Available', 'Always Available'), ('Active', 'Active'), ('Inactive', 'Inactive')], default='Always Active', max_length=20)),
                ('retention_count', models.CharField(default=0, max_length=220)),
                ('action', models.CharField(choices=[('Delete Permently', 'Delete Permently'), ('Set Inactive', 'Set Inactive')], max_length=20)),
                ('period', models.CharField(choices=[('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months')], default='Days', max_length=20)),
                ('entry_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(blank=True, max_length=220)),
                ('file_id', models.CharField(default='NA', max_length=220)),
                ('folder_id', models.CharField(blank=True, max_length=220)),
                ('upload_file', models.FileField(upload_to='')),
                ('file_name', models.CharField(blank=True, max_length=220, null=True)),
                ('tags', models.CharField(blank=True, max_length=220, null=True)),
                ('document_id', models.CharField(blank=True, max_length=220, null=True)),
                ('signed_by', models.CharField(blank=True, max_length=220, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('related_file', models.FileField(blank=True, upload_to='')),
                ('new_upload', models.FileField(blank=True, null=True, upload_to='')),
                ('entry_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(blank=True, max_length=220)),
                ('folder_name', models.CharField(max_length=220)),
                ('retention', models.CharField(choices=[('Always Available', 'Always Available'), ('Active', 'Active'), ('Inactive', 'Inactive')], default='Always Available', max_length=20)),
                ('retention_count', models.CharField(default=0, max_length=220)),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('action', models.CharField(choices=[('Delete Permently', 'Delete Permently'), ('Set Folder Inactive', 'Set Folder Inactive')], default='Set Folder Inactive', max_length=20)),
                ('period', models.CharField(choices=[('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months')], default='Days', max_length=20)),
                ('entry_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VersionUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_upload', models.FileField(upload_to='')),
                ('department_id', models.CharField(blank=True, max_length=220)),
                ('file_id', models.CharField(default='NA', max_length=220)),
                ('folder_id', models.CharField(blank=True, max_length=220)),
                ('document_id', models.CharField(blank=True, max_length=220, null=True)),
                ('entry_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
