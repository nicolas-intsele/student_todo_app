from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView, name='task_list'),
    path('task/add/', views.TaskCreateView, name='task_create'),
    path('task/<int:pk>/', views.TaskDetailView, name='task_detail'),
    path('task/<int:pk>/edit/', views.TaskUpdateView, name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView, name='task_delete'),
    path('task/<int:pk>/toggle/', views.ToggleTaskCompleteView, name='task_toggle'),
]