from django.db import models

# Create your models here.
class ProductCarousel(models.Model):
    caption = models.CharField(max_length=255,default=None)
    large_file = models.FileField(upload_to='static/videos/',default=None)
    small_file= models.FileField(upload_to='static/videos/',default=None)
    name = models.CharField(max_length=255,default=None)
    def __str__(self):
        return self.name
    


class CollectionCarousel(models.Model):
    caption = models.CharField(max_length=255)
    large_file = models.FileField(upload_to='static/videos/',default=None)
    small_file= models.FileField(upload_to='static/videos/',default=None)
    name = models.CharField(max_length=255,default=None)
    def __str__(self):
        return self.name




class PromotionCarousel(models.Model):
    caption = models.CharField(max_length=255,default=None)
    large_file = models.FileField(upload_to='static/videos/',default=None)
    small_file= models.FileField(upload_to='static/videos/',default=None)
    name = models.CharField(max_length=255,default=None)
    def __str__(self):
        return self.name 