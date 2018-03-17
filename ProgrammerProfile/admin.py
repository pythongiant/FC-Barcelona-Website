from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Posts)
