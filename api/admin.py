from django.contrib import admin

# Register your models here.

from .models import Task
from .models import Apidata

admin.site.register(Task)
admin.site.register(Apidata)