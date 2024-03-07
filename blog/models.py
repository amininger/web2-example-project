from django.db import models

class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(blank=True)
    pub_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    num_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ("*" if self.is_published else "")