from django.contrib import admin
from .models import Post

# Register your models here.
# register db in the admin url
admin.site.register(Post)