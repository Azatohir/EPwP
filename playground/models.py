from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

class Note(TimeStampedModel, MPTTModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = TreeForeignKey(Topic, null=True, blank=True, related_name='notes', db_index=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title