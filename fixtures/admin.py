from django.contrib import admin
from fixtures.models import Fixture

class AdminFixture(admin.ModelAdmin):
	list_display = ('id', 'date', )

admin.site.register(Fixture, AdminFixture)