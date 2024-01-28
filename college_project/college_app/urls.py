from django.urls import path
from . import views

app_name = 'college_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('user_info/', views.user_info, name='user_info'),
    path('logout/', views.user_logout, name='logout'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('<slug:d_slug>/', views.dept_detail, name='department'),
]

