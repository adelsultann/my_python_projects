from django.urls import path

from. import views
urlpatterns = [
    # as_view() to use Class inside the url,
    path("", views.home, name="home"),
    path('task/<int:pk>/', views.task_details, name='task'),
    path('task-create', views.Task_create, name='task-create'),
    path('task-update/<int:pk>/', views.Task_update, name='task-update'),
    path('task-delete/<int:pk>/', views.Delete_task, name='task-delete'),
    path("register/", views.registerPage, name="register"),
    path("login/", views.LoginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),

    # path('task-create', TaskCreate.as_view(), name='task-create'),
    # path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    # path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),

]
