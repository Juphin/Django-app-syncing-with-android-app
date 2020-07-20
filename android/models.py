from django.db import models
from django.utils import timezone
# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
