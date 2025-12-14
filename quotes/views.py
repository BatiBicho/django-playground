from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.

quotes_week = {
    "monday": "Frase del lunes",
    "tuesday": "Frase del martes",
    "wednesday": "Frase del miercoles",
    "thursday": "Frase del jueves",
    "friday": "Frase del viernes",
    "saturday": "Frase del sabado",
    "sunday": "Frase del domingo"
}


def index(request):
    days = list(quotes_week.keys())
    return render(request, 'quotes/index.html', {
        'days_list': days
    })


def days_week(request, day):
    try:
        quote_day = quotes_week[day]
        return HttpResponse(quote_day)
    except:
        # return HttpResponseNotFound("Dia no encontrado")
        raise Http404()


def days_week_with_number(request, day):
    days = list(quotes_week.keys())
    if day < 1 or day > len(days):
        # return HttpResponseNotFound("Dia no encontrado")
        raise Http404()

    redirected_day = days[day - 1]
    redirected_path = reverse("quote-day", args=[redirected_day])
    return HttpResponseRedirect(redirected_path)
