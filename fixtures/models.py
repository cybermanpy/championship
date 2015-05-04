from django.db import models

class Fixture(models.Model):
	date = models.CharField(blank=False, max_length=50)
	class Meta:
	    verbose_name = 'Fixture'
	    verbose_name_plural = 'Fixtures'
	def __unicode__(self):
		return self.date