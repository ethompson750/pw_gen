from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase', False):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers', False):
        characters.extend('1234567890')

    if request.GET.get('special', False):
        characters.extend('!@#$%^&*()')

    pwd = ''

    for _ in range(length):
        pwd += random.choice(characters)


    return render(request, 'generator/password.html', {'password': pwd})