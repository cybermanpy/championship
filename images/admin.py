from django.contrib import admin
from images.models import Image

class AdminImage(admin.ModelAdmin):
	list_diaplay = ('id', 'title', 'imagesource', 'fkevent', )
	list_filter = ('fkevent',)

admin.site.register(Image, AdminImage)