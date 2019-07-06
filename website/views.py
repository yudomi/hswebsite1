from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json

# Create your views here.
def home(request):
    context = locals()
    layout = 'home.html'
    return render(request, layout, context)

@csrf_exempt
def login(request):
    username = json.loads(request.body)['username']
    password = json.loads(request.body)['password']

    print(username)
    print(password)

    if username == 'test' and password == '1234':
        return JsonResponse({'success':True})
    else :
        return JsonResponse({'success':False})

@csrf_exempt
def login_success(request):
    context = locals()
    layout = 'success.html'
    return render(request, layout, context)