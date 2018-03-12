from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('bio/', views.bio, name='bio'),
    path('tech-tips/', views.techTips, name='tech tips'),
]