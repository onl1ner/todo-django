from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.creation_form, name='add'),
    path('finish/<task_id>', views.finish, name='finish'),
    path('clear', views.clear_list, name='clear'),
    path('logout_user', views.logout_user, name='logout_user')
]