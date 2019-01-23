from django.contrib import admin
from .models import Meeting,Minutes,Event,Resource 
# Register your models here.

admin.site.register(Meeting)
admin.site.register(Resource)
admin.site.register(Event)
admin.site.register(Minutes)