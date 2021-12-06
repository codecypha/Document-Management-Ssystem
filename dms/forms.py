from django import forms
from django.forms import ModelForm
from .models import Department,  Folder, FileType, VersionUpload, GroupManagement, AddUserGroup, AddUserDept, AddUserFolder
class DepartmentForm(forms.ModelForm):  
    class Meta:
        model = Department
        fields = ('__all__')
        exclude=['country', 'status']

        
class FolderForm(forms.ModelForm):  
    class Meta:
        model = Folder
        fields = ('__all__')
        exclude=['document_id','status', 'group_name']


class FileForm(forms.ModelForm):  
    class Meta:
        model = FileType
        fields = ('__all__')
        exclude=['file_id', 'document_id']


class VersionForm(forms.ModelForm):  
    class Meta:
        model = VersionUpload
        fields = ('__all__')
        exclude=['document_id', 'file_id']



class ManagementForm(forms.ModelForm):
    class Meta:
        model = GroupManagement
        fields = '__all__'
        exclude=['creator']
    

class AddUserForm(forms.ModelForm):
    class Meta:
        model = AddUserGroup
        fields = '__all__'
        #exclude=['group_name']


class AddUserDeptForm(forms.ModelForm):
    class Meta:
        model = AddUserDept
        fields = '__all__'
        #exclude=['group_name']AddUserFolderForm
        

class AddUserFolderForm(forms.ModelForm):
    class Meta:
        model = AddUserFolder
        fields = '__all__'
        #exclude=['group_name']