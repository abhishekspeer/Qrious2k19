from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    if(request.method == 'POST'):
        return redirect('/accounts/google/login')
    return render(request, 'index.html')


def loading(request):
    print(request.user)
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
