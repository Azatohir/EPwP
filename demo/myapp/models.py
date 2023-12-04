from django_extensions.db.models import TimeStampedModel
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Topic(TimeStampedModel, MPTTModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='nothing', on_delete=models.CASCADE)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()

    def __str__(self):
        return self.title