from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    list_items = ""
    days = list(quotes_week.keys())  # [monday, tuesday, ...]

    for day in days:
        day_path = reverse("quote-day", args=[day])
        list_items += f'<li><a href="{day_path}">{day}</a></li>'
    response_html = f"<ul>{list_items}</ul>"
    return HttpResponse(response_html)


def days_week(request, day):
    try:
        quote_day = quotes_week[day]
        return HttpResponse(quote_day)
    except:
        return HttpResponseNotFound("Dia no encontrado")


def days_week_with_number(request, day):
    days = list(quotes_week.keys())
    if day < 1 or day > len(days):
        return HttpResponseNotFound("Dia no encontrado")
    redirected_day = days[day - 1]
    redirected_path = reverse("quote-day", args=[redirected_day])
    return HttpResponseRedirect(redirected_path)
