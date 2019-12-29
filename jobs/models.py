from django.db import models
from datetime import datetime

class Job(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images/', blank=True)
    summary = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def customized_date(self):
        return self.pub_date.strftime('%Y')
