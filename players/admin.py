from django.contrib import admin
from players.models import Player

class AdminPlayer(admin.ModelAdmin):
	list_display = ('id', 'name', 'goals', 'cedula', 'agent', 'subagent', 'captain', )
	list_filter = ('fkteam',)

admin.site.register(Player, AdminPlayer)