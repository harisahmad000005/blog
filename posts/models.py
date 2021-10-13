from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

ACTIVE_CHOICES = (
    ('publish','Publish'),
    ('unpublish','Unpublish'),
)


class Posts(models.Model):
    title = models.CharField(max_length=150,null=True,blank=True)
    author_name = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=500,null=True,blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    active = models.CharField(max_length=10, choices=ACTIVE_CHOICES, default='green')
    def __str__(self):
        if self.title:
            return self.title
        else:
            return "-"
    def get_absolute_url(self):
        return reverse('postDetail', kwargs={'pk':self.id})

class PostComments(models.Model):
    post = models.ForeignKey(Posts, related_name='comments' ,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-Comment By:-{}'.format(self.post.title, self.name.username)
