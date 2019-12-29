from django.db import models
from datetime import datetime

class Job(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def customized_date(self):
        return self.pub_date.strftime('%Y')
