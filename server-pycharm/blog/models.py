from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # author = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.SET_NULL,)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("{} by {}").format(self.title, self.name)

    def summary(self):
        return self.content[:100]