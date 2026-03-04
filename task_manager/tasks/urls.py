from tasks.views import register, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', TaskListView.as_view(), name='tasks'),

    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),

    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]