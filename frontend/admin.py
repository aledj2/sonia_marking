from django.contrib import admin
import autocomplete_light

from .models import *

admin.site.register(Classes)
admin.site.register(Students)
admin.site.register(BookMarked)
