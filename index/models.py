from django.db import models
from time import gmtime, strftime


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    def __str__(self):
        return self.title
