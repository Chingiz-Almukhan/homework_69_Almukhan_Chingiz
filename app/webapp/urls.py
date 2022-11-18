from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from webapp.views import add_view, subtract_view, multiply_view, divide_view

urlpatterns = [
    path('add/', csrf_exempt(add_view)),
    path('subtract/', csrf_exempt(subtract_view)),
    path('multiply/', csrf_exempt(multiply_view)),
    path('divide/', csrf_exempt(divide_view)),
]
