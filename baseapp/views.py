# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import myuser, questions, choice
from django.shortcuts import render

def login(request):
    return render(request, 'login.html', context)


def roulette(request):
    #if request:
        #username
    return render(request, 'roulette.html', context)

def description(request):
    #if request:
        #level_id
    return render(request, 'description.html', context)

def question(request):
    #send all questions and choices based on ID
    return render(request, 'question.html', context)

def afteranswer(request):
    #if request:
        #check choice id matches with correct choice
        #if yes, increment user.marks else lite
    # if request.method == POST:
    #     selectedchoice = request.POST.get('selected_choice')
    #     question = get_object_or_404(Question, pk=question_id)
    #     correctchoice = question.
    return render(request, 'onanswer.html', context)

def leaderboard(request):
    userlist = user.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', context)
