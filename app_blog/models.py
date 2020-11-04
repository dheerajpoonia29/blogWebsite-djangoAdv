from django.db import models
from app_user.models import User

class Author(models.Model):
	id = models.AutoField(primary_key=True)
	# user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=False, unique=True)
	# UNIQUE TRUE HAS SAME EFFECT AS ONETOONE FIELD
	user_id = models.OneToOneField('User', on_delete=models.CASCADE)
	
	# update role of user to author
	# user = User.objects.get(id=user_id)
	# TODO: do this from view


	# Author to all blog
		# no need of these relationship
			# blog_id = models.ManyToManyField('Blog')
			# blog_id = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True)
		# get from blog foreign key
			# >>> obj = Author.objects.get(id=1).author_blog.all()
			# >>> for q in obj:
			# ...     print(q.id, q.title)

class Blog(models.Model):
	id = models.AutoField(primary_key=True)

	class Category(models.IntegerChoices):
		sports = 0
		music = 1
		food = 2
		education = 3	

	category = Category.music	
	pub_date = models.DateField(auto_now=True)

	# many to one -> foreign key
	author_id = models.ForeignKey('Author', on_delete=models.CASCADE, null=False, related_name='author_blog')
	# rating_id = models.ManyToManyField('Rating')
	rating_id = models.ForeignKey('Rating', on_delete=models.CASCADE, null=True)

	title = models.CharField(max_length=200, null=False)
	body = models.CharField(max_length=500, null=False)

class Rating(models.Model):
	id = models.AutoField(primary_key=True)
	blog_id = models.ForeignKey('Blog', on_delete=models.CASCADE)
	user_id = models.ForeignKey('User', on_delete=models.CASCADE)
	star = models.IntegerField()
	feedback_content = models.CharField(max_length=200)
