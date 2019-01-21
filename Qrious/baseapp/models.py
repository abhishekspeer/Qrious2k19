# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class myuser(models.Model):
    Name = models.CharField(max_length=100)
    bits_id = models.CharField(max_length=100, unique=True)
    score = models.IntegerField()

class questions(models.Model):
    question = models.CharField(max_length=250, unique=True)
    question_id = models.PositiveIntegerField(default=1000)
    question_level = models.PositiveIntegerField(default=1000)

class choice(models.Model):
    choice_id = models.PositiveIntegerField()
    question = models.ForeignKey(questions, on_delete = models.CASCADE)
    choice = models.CharField(max_length=100)
