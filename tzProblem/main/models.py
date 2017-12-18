from django.db import models


# Create your models here.
class Article(models.Model):
    pubDateTime = models.DateTimeField()    # Publishing date time

    def __str__(self):
        return str(self.pubDateTime)
