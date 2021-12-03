
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('department/', views.department, name='department'),
   path('edit-department/<str:pk>/', views.edit_department, name='edit_department'),
   path('delete-department/<str:pk>/', views.delete_department, name='delete_department'),
   path('view-department/<str:pk>/', views.view_department, name='view_department'),
   path('folder/<str:pk>/', views.folder, name='folder'),
   path('edit-folder/<str:pk>/', views.edit_folder, name='edit_folder'),
   path('delete-folder/<str:pk>/', views.delete_folder, name='delete_folder'),
   path('delete-file/<str:pk>/', views.delete_file, name='delete_file'),
   path('view-file/<str:pk>/', views.view_file, name='view_file'),
   path('edit-file/<str:pk>/', views.edit_file, name='edit_file'),
   path('upload_version/', views.upload_version, name='upload_version'),
   path('create-group/', views.CreateGroup, name='create'),
   path('add_to_group/<str:pk>/', views.add_to_group, name='add_to_group'),
   path('searchdoc/', views.searchdoc, name='searchdoc'),
   path('login/', views.loginPage, name='login'),
   path('logout/', views.logoutPage, name='logout'),
]
