from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard')
]
