from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.jpg' , upload_to = 'profile_pics')
	city = models.CharField(max_length = 50)
	fav_club = models.CharField(max_length = 50)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(force_insert=False)

		img = Image.open(self.image.path)
		if img.height>300 or img.width>300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)
			
