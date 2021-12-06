from django.db import models

# Create your models here.

class Department(models.Model):
    author = models.CharField(max_length=220, blank = True)
    department_name = models.CharField(max_length=220, unique=True)
    retention_choices = [
        ('Inactive', 'Inactive'),
        ('Always Available', 'Always Available'),
    ]
    retention = models.CharField(
        max_length=20,
        choices= retention_choices,
        default = 'Inactive'
    )

    retention_count = models.CharField(max_length=220, default=0)
    
    action_choices = [
        ('Delete Permently', 'Delete Permently'),
        ('Set Inactive', 'Set Inactive'),
    ]
    action = models.CharField(
        max_length=20,
        choices= action_choices,
        default = 0
       
    )

    period_choices = [
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'), 
    ]
    period = models.CharField(
        max_length=20,
        choices= period_choices,
        default = 'Days'
        
    )
    country = models.CharField(max_length=25, default='Nigeria')
    group_name = models.CharField(max_length=125, blank=True)
    entry_date  = models.DateField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, default='active')
    def __str__(self):
        return self.retention



class Folder(models.Model):
    author = models.CharField(max_length=220, blank = True)
    department_id = models.CharField(max_length=220, blank=True)
    folder_name = models.CharField(max_length=220)
    retention_choices = [
        ('Inactive', 'Inactive'),
        ('Always Available', 'Always Available'),
 
    ]
    retention = models.CharField(
        max_length=20,
        choices= retention_choices,
        default = 'Inactive'
    )
    retention_count = models.CharField(max_length=220, default=0)
    upload_file = models.FileField(blank = True)
    action_choices = [
        ('Delete Permently', 'Delete Permently'),
        ('Set Folder Inactive', 'Set Folder Inactive'),
    ]
    action = models.CharField(
        max_length=20,
        choices= action_choices,
        default = 'Set Folder Inactive',
    )

    period_choices = [
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'), 
    ]
    period = models.CharField(
        max_length=20,
        choices= period_choices,
        default = 'Days'
    )

    approver = models.CharField(max_length=220, blank=True, null=True)
    status = models.CharField(max_length=10, default='Pending')
    group_name = models.CharField(max_length=125, )
    entry_date  = models.DateField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.folder_name



class FileType(models.Model):
    author = models.CharField(max_length=220, blank = True)
    #department = models.ForeignKey("Department", on_delete=models.CASCADE)
    department_id = models.CharField(max_length=220, blank=True)
    file_id = models.CharField(max_length=220, blank=True)
    folder_id = models.CharField(max_length=220, blank=True)
    upload_file = models.FileField(blank=True)
    file_name = models.CharField(max_length=220, blank=True, null=True)
    tags = models.CharField(max_length=220, blank=True, null=True)
    #tags = TaggableManager()
    document_id = models.CharField(max_length=220, blank=True, null=True)
    signed_by = models.CharField(max_length=220, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    related_file = models.FileField(blank = True)
    new_upload = models.FileField(blank=True, null=True)
    entry_date  = models.DateTimeField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.file_id


class VersionUpload(models.Model):
    author = models.CharField(max_length=220, blank = True)
    new_upload = models.FileField()
    department_id = models.CharField(max_length=220, blank=True)
    file_id = models.CharField(max_length=220, default='NA')
    folder_id = models.CharField(max_length=220, blank=True)
    document_id = models.CharField(max_length=220, blank=True, null=True)
    entry_date  = models.DateTimeField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.file_id


class Approvals(models.Model):
    author = models.CharField(max_length=220, blank = True)
    department_id = models.CharField(max_length=220, blank=True)
    file_id = models.CharField(max_length=220, default='NA')
    folder_id = models.CharField(max_length=220, blank=True)
    document_id = models.CharField(max_length=220, blank=True, null=True)
    approver = models.CharField(max_length=220, blank=True, null=True)
    status = models.CharField(max_length=10, default='Pending')
    entry_date  = models.DateTimeField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.file_id



class GroupManagement(models.Model):
    group_name = models.CharField(max_length=200)
    creator = models.CharField(max_length=120)
    entry_date  = models.DateField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.group_name
    class Meta:
        db_table = 'groupmanagement'


class AddUserGroup(models.Model):
    group_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    creator = models.CharField(max_length=120)
    entry_date  = models.DateField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.username
 
class AddUserDept(models.Model):
    department_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    dept_access = models.CharField(max_length=5, default='full')
    creator = models.CharField(max_length=120)
    entry_date  = models.DateField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.department_name
  
    
class AddUserFolder(models.Model):
    department_name = models.CharField(max_length=200)
    folder_name = models.CharField(max_length=200)
    folder_access = models.CharField(max_length=5, default='full')
    username = models.CharField(max_length=200)
    creator = models.CharField(max_length=120)
    entry_date  = models.DateField(auto_now=True)
    update_date  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.folder_name