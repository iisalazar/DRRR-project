from django.db import models

# Create your models here.
class Content(models.Model):
	header = models.CharField(max_length=100, blank=False, null=False)
	body = models.TextField(blank=False, null=False)
	date_created = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse()

	def __str__(self):
		return self.header

	class Meta:
		ordering = ['-date_created']

