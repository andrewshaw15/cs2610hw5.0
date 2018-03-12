from django.shortcuts import render

from time import strftime

def main(request):
    return render(request, 'blog/main.html', { 'current_time' : strftime('%c') })

def bio(request):
    return render(request, 'blog/bio.html', { 'current_time' : strftime('%c') })

def techTips(request):
    return render(request, 'blog/tech-tips.html', { 'current_time' : strftime('%c') })
