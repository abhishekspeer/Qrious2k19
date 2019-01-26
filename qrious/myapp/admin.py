from django.contrib import admin
from myapp.models import Userdata,Level,Question,Choice

# Register your models here.
admin.site.register(Userdata)
admin.site.register(Question)
admin.site.register(Level)
admin.site.register(Choice)
