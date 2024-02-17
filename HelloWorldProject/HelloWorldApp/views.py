from django.shortcuts import render

from django.http import JsonResponse

def hello_world(request):
    response_data = {'Message': 'Hello World!'}
    return JsonResponse(response_data)

