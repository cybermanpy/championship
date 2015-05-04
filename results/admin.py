from django.contrib import admin
from results.models import Result

class AdminResult(admin.ModelAdmin):
	list_display = ('id', 'description')

admin.site.register(Result, AdminResult)