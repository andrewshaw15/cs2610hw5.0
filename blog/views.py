from django.shortcuts import render, redirect

from time import strftime

def main(request):
    return render(request, 'blog/main.html', { 'current_time' : strftime('%c') })

def bio(request):
    return render(request, 'blog/bio.html', { 'current_time' : strftime('%c') })

def techTips(request):
    return render(request, 'blog/tech-tips.html', { 'current_time' : strftime('%c') })

def starWars(request):
    return redirect('http://www.starwars.com/')

def airForce(request):
    return redirect('http://www.af.mil/')

def usu(request):
    return redirect('https://www.usu.edu/')

def commonGitCommands(request):
    return redirect('http://guides.beanstalkapp.com/version-control/common-git-commands.html')

def basicGitCommands(request):
    return redirect('https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html')

def gitReference(request):
    return redirect('https://git-scm.com/docs')
