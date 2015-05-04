from django.db import models

class Result(models.Model):
	description = models.CharField(blank=False, max_length=50)
	class Meta:
	    verbose_name = 'Result'
	    verbose_name_plural = 'Results'
	def __unicode__(self):
		return self.description