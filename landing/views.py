from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.


def home(request):
    return render(request, 'landing/landing.html', {
        'name': 'Juan Perez',
        'today': date.today(),
    })
