from django.db import models

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50, unique=True, null=False)
	password = models.CharField(max_length=50)
	role = models.IntegerField(default=0)
	# 0-admin, 1-blog

	def __str__(self):
		return str(self.id)+', '+self.name+', '+self.email+', '+self.password