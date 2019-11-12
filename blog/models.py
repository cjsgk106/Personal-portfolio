from django.db import models

class Myr(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50] + '...'

    def customized_date(self):
        return self.pub_date.strftime('%b %e %Y')

class Mysql(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50] + '...'

    def customized_date(self):
        return self.pub_date.strftime('%b %e %Y')

# Create your models here.
# title
# pub_date
# body
# image

# Add the Blog app to the settings

# Create a migration

# Migrate

# add to the admin
