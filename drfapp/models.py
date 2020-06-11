from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
	created_by     = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	content        = models.TextField()
	created_date   = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):

		return str(self.created_by)

	def clean(self):
		number = self.content
		if len(number)<5:
			raise ValidationError("plz 5 up Character")
		else:
		   print('Better')	


     
class AuthorProfile(models.Model):
	user          = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	profile_image = models.ImageField()
	first_name    = models.CharField(max_length=200)
	last_name     = models.CharField(max_length=200)


	def __str__(self):

		return str(self.first_name)
