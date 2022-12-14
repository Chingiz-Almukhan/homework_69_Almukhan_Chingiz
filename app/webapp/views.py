import json

from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView


def add_view(request, *args, **kwargs):
    response = {}
    if request.method == 'POST' and request.body:
        try:
            data = json.loads(request.body)
            sum = float(data['A']) + float(data['B'])
            response['result'] = json.loads(str(sum))
            return JsonResponse(response)
        except ValueError:
            response = JsonResponse({"error": "Division by zero!"})
            response.status_code = 400
            return response


def subtract_view(request, *args, **kwargs):
    response = {}
    if request.method == 'POST' and request.body:
        try:
            data = json.loads(request.body)
            sum = float(data['A']) - float(data['B'])
            response['result'] = json.loads(str(sum))
            return JsonResponse(response)
        except ValueError:
            response = JsonResponse({"error": "Division by zero!"})
            response.status_code = 400
            return response


def multiply_view(request, *args, **kwargs):
    response = {}
    if request.method == 'POST' and request.body:
        try:
            data = json.loads(request.body)
            sum = float(data['A']) * float(data['B'])
            response['result'] = json.loads(str(sum))
            return JsonResponse(response)
        except ValueError:
            response = JsonResponse({"error": "Division by zero!"})
            response.status_code = 400
            return response


def divide_view(request, *args, **kwargs):
    response = {}
    if request.method == 'POST' and request.body:
        try:
            data = json.loads(request.body)
            sum = float(data['A']) / float(data['B'])
            response['result'] = json.loads(str(sum))
            return JsonResponse(response)
        except ValueError:
            response = JsonResponse({"error": "Division by zero!"})
            response.status_code = 400
            return response


class IndexView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return redirect('main')
