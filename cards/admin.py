from django.contrib import admin
from cards.models import Card, CardPlayer

class CardAdmin(admin.ModelAdmin):
	list_display = ('id', 'description',)

class CardPlayerAdmin(admin.ModelAdmin):
	list_display = ('fkcard', 'fkplayer','fkfixture')

admin.site.register(Card, CardAdmin)
admin.site.register(CardPlayer, CardPlayerAdmin)