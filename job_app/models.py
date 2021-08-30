from django.db import models

# Create your models here.
class Job(models.Model):
    summary = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog_images/")


    def __str__(self):
        return self.summary
