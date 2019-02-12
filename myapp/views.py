from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Userdata,Level,Choice,Question
from django.http import Jsonresponse
import json

# Create your views here.


def home(request):
    if(request.method == 'POST'):
        return redirect('/accounts/google/login')
    return render(request, 'index.html')


def loading(request):
    return render(request, 'loader.html')


def roulette(request):
    return render(request, 'roulette.html')


def l_out(request):
    logout(request)
    return redirect('/')


def quiz(request, filename):
    print("This function.")
    return render(request, filename)


def postanswer(request, filename):
    if request.method == 'POST':
        print(request.POST)
    return HttpResponse('')

def leaderboard(request):
    data_get = json.loads(request.body.decode('utf-8'))
    data = []
    list = Userdata.objects.order_by('-score')[:10]
    for user in list:
        user_details["details"]={
        "name" = Userdata.name
        "ID" = Userdata.bits_id
        "score" = Userdata.score
        }
        data.append(user_details)

    x = Userdata.objects.get(bitsid=data_get['bits_id'])
        user_details["details"]={
        "name" = x.name
        "ID" = x.bits_id
        "score" = x.score
        }
          data.append(user_details)
    return Jsonresponse(data, safe=false)
