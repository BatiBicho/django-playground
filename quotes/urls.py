from django.urls import path
from . import views

# Tomar en cuenta el orden de las rutas
urlpatterns = [
    path('', views.index),
    path('<int:day>', views.days_week_with_number),
    path('<str:day>', views.days_week, name="quote-day"),
]
