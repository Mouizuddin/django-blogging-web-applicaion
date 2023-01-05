from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_of_post = models.DateTimeField(default=timezone.now)
    post_author = models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
# In [2]: from django.contrib.auth.models import User

# In [3]: from django.db import models

# In [4]: from blog_app.models import Post
