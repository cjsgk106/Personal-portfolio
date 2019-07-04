from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
# Create your models here.
# title
# pub_date
# body
# image

# Add the Blog app to the settings

# Create a migration

# Migrate

# add to the admin
