from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.


def home(request):
    stack_list = [{"id": "django", "name": "Django"},
                  {"id": "python", "name": "Python"},]

    return render(request, 'landing/landing.html', {
        'name': 'Bicho',
        'today': date.today(),
        'stack': stack_list
    })


def stack_detail(request, tool):
    return HttpResponse(f"Tecnología: {tool}")
