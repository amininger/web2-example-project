from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    class Meta:
        permissions = [
            ("publish_blogpost", "Can publish a BlogPost")
        ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(blank=True)
    pub_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    num_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ("*" if self.is_published else "")

    def get_absolute_url(self):
        return "/blog/post/" + str(self.id) + "/"

