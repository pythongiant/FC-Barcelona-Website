from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person,Posts
admin.site.register(Person)
admin.site.register(Posts)
