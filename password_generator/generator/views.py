from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'vq13498qregb'})

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    pwd = ''

    for _ in range(length):
        pwd += random.choice(characters)


    return render(request, 'generator/password.html', {'password': pwd})