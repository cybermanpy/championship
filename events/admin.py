from django.contrib import admin
from events.models import Event

class AdminEvent(admin.ModelAdmin):
	list_display = ('id', 'fkusr', 'name', 'description', 'status')

admin.site.register(Event, AdminEvent)
