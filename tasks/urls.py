from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('api/tasks/', api.TaskListCreateAPIView.as_view(), name='api-tasks-list-create'),
    path('api/tasks/<int:pk>/', api.TaskRetrieveUpdateDestroyAPIView.as_view(), name='api-tasks-detail'),
        path('', views.TaskList.as_view(), name='tasks_list'),
    path('tasks/create/', views.TaskCreate.as_view(), name='task_create'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('tasks/<int:pk>/edit/', views.TaskUpdate.as_view(), name='task_edit'),
]
