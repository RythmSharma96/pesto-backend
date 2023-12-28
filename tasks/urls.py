from django.urls import path
from .views import TaskList, Tasks, TaskCreate

urlpatterns = [
    path('taskList/', TaskList.as_view()),
    path('task/<int:pk>/', Tasks.as_view()),
    path('task', TaskCreate.as_view())
]
