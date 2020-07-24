from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    shortDescription = models.TextField()
    longDescription = models.TextField()
    technology = models.TextField()
    image = models.FilePathField(path='/img')
    videoURL = models.TextField()
    projectLink = models.TextField()

    def __str__(self):
        return self.title
