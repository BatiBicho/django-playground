from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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


def days_week(request, day):
    try:
        quote_day = quotes_week[day]
        return HttpResponse(quote_day)
    except:
        return HttpResponseNotFound("Dia no encontrado")


def days_week_with_number(request, day):
    return HttpResponse(f"El numero del dia es: {day}")
