from django.contrib import admin
from teams.models import Team

class AdminTeam(admin.ModelAdmin):
	list_display = ('id', 'description', 'score', 'gf', 'gc', 'pj', 'pg', 'pe', 'pp', 'fkevent')
	list_filter = ('fkevent',)

admin.site.register(Team, AdminTeam)