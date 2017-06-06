from django.contrib import admin
from blogs.models import User, Blog, Post, SubscribeBlog, MarkPost

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(SubscribeBlog)
admin.site.register(MarkPost)

