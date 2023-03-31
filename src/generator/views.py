from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def description(request):
    return render(request, 'generator/description.html')


def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    try:
        length = int(request.GET.get('length'))
    except ValueError:
        length = 12
    thepass = ''
    print(length)
    for ch in range(length):
        thepass += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepass})
