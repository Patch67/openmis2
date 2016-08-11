from django.contrib import admin

from .models import Room
from import_export import resources


admin.site.register(Room)
