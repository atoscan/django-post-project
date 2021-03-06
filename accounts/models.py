from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	bio = models.CharField(max_length = 255, default = '')
	website = models.URLField(default = '', blank=True)
	nickname = models.CharField(max_length = 50, default = 'user', blank=True)
	#image = models.ImageField(upload_to='profile_image', blank=True)


	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User)