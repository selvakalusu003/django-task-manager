from django.contrib import admin
from django.urls import path
from tasks.views import register, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, mark_complete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', TaskListView.as_view(), name='tasks'),

    path('task/create/', TaskCreateView.as_view(), name='task-create'),

    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),

    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    path('task/<int:pk>/complete/', mark_complete, name='task-complete'),
]

