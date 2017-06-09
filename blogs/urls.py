from django.conf.urls import url
from .views import AddPostView, TapeUserView, PostsBlogView, AddSubscribeBlogView, DelSubscribeBlogView

from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import User, Blog, Post

urlpatterns = [
    url(r'^tape_user/(?P<user_id>\d+)/$', TapeUserView.as_view(template_name = 'blogs/tape_user.html'), name = 'tape_user'),
    url(r'^blog/(?P<blog_id>\d+)/$', PostsBlogView.as_view(template_name = 'blogs/blog.html'), name = 'blog'),
    url(r'^add_post/(?P<blog_id>\d+)/$', AddPostView.as_view(template_name = 'blogs/add_post.html'), name = 'add_post'),
    # url(r'^edit_post/(?P<post_id>\d+)/$', EditPostView.as_view(template_name = 'blogs/edit_post.html'), name = 'edit_post'),
    # url(r'^del_post/(?P<post_id>\d+)/$', DelPostView.as_view(template_name = 'blogs/del_post.html'), name = 'del_post'),
    url(r'^del_post/(?P<pk>\d+)/$', DeleteView.as_view(model = Post, template_name = 'blogs/del_post.html', success_url = '/'), name = 'del_post'),
    url(r'^add_subscribe_blog/(?P<user_id>\d+)/(?P<blog_id>\d+)/$', AddSubscribeBlogView, name = 'add_subscribe_post'),
    url(r'^del_subscribe_blog/(?P<user_id>\d+)/(?P<blog_id>\d+)/$', DelSubscribeBlogView, name = 'del_subscribe_post'),

    # url(r'^edit_post/(?P<pk>\d+)/$', UpdateView.as_view(model = Post, template_name = 'blogs/edit_post.html', success_url = '/'), name='edit_post'),

    url(r'^$', ListView.as_view(model = User, context_object_name = 'users', template_name = 'blogs/home.html'), name = 'home')
]
