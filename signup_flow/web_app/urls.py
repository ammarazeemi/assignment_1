from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='signup'),
        path('signin/', views.signin, name='signin'),
        path('verification/', views.email_authenticate, name='email_authenticate'),
        path('authorization/', views.authorization, name='authorization'),
        path('records/', views.records, name='records'),
        path('change_password', views.change_password, name='change_pass')
        
]