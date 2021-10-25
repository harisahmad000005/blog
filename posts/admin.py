from django.contrib import admin

from .models import Posts, PostComments

# Register your models here.

admin.site.register(Posts)
admin.site.register(PostComments)