from django.db import models
import datetime

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now()) # was initally through auto_now_add but resulted in the wrong TZ
    updated_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.title