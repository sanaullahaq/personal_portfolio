from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')  # the images will uploaded to the mentioned directory
    url = models.URLField(blank=True)  # blank=True parameter means we can insert any type of data here

    def __str__(self):
        return self.title
