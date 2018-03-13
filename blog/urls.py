from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('bio/', views.bio, name='bio'),
    path('tech-tips/', views.techTips, name='tech tips'),
    path('star-wars/', views.starWars, name='star wars'),
    path('air-force/', views.airForce, name='air force'),
    path('usu/', views.usu, name='usu'),
    path('common-git-commands/', views.commonGitCommands, name='common git commands'),
    path('basic-git-commands/', views.basicGitCommands, name='basic git commands'),
    path('git-reference/', views.gitReference, name='git reference'),
]
