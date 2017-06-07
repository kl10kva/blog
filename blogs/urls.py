from django.conf.urls import url
from .views import CreatePostView

from django.views.generic import ListView, DetailView
from .models import User

urlpatterns = [
    url(r'^tape_user/(?P<pk>\d+)/$', DetailView.as_view(model = User, template_name = 'blogs/tape_user.html'), name = 'tape_user'),
    url(r'^add_post/$', CreatePostView.as_view(template_name = 'blogs/add_post.html'), name = 'add_post'),
    url(r'^$', ListView.as_view(model = User, context_object_name = 'users', template_name = 'blogs/home.html'), name = 'home')
]
