from django.db import models
import datetime
from django.utils.text import slugify
# Create your models here.
class Blog(models.Model):
    title = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(blank=True,null=True)
    pub_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="blog_images/")

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title
