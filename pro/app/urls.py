from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signup_action', views.signup_action, name='signup_action'),
    path('login', views.login, name='login'),
    path('login_action', views.login_action, name='login_action'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('add_emp_action', views.add_emp_action, name='add_emp_action'),
    path('view_all_emp', views.view_all_emp, name='view_all_emp'),
    path('update_emp/<int:id>', views.update_emp, name='update_emp'),
    path('update_emp_action/<int:id>', views.update_emp_action, name='update_emp_action'),
    path('delete_emp/<int:id>', views.delete_emp, name='delete_emp'),
]
