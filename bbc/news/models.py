from django.db import models
from django.conf import settings
import datetime
# Create your models here.
User = settings.AUTH_USER_MODEL

class Newspaper(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=500, unique=True, blank=False, null=False)
	text = models.TextField(blank=False, null=False)
	image = models.ImageField(null=True, blank=True, default='default.png')
	date = models.DateTimeField(default=datetime.datetime.now())

	def __str__(self):
		return self.title
























