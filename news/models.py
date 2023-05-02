from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=1000)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title
