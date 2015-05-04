from django.contrib import admin
from matches.models import Match

class AdminMatch(admin.ModelAdmin):
	list_display = ('id', 'fkhome', 'fkaway', 'fkresult', 'fkfixture', 'goalshome', 'goalsaway', )
	list_filter = ('fkfixture', 'fkresult',)

admin.site.register(Match, AdminMatch)