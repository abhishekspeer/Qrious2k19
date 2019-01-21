# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import questions, myuser, choice

# Register your models here.
admin.site.register(questions)
admin.site.register(myuser)
admin.site.register(choice)
