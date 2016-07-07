from django.db import models
from django.utils import timezone

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=30)
    pub_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __get_content__(self):
        if len(self.content)<80:
            return self.content
        else:
            return self.content[:77] + '...'

    def __str__(self):
        return self.title
