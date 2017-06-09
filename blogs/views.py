from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import User, Blog, Post, SubscribeBlog, MarkPost


class TapeUserView(TemplateView):
    """Профиль пользователя"""

    def get_context_data(self, user_id):
        my_blog = Blog.objects.get(user_id = user_id)
        context = super(TapeUserView, self).get_context_data()
        context = {
            'my_blog': my_blog,
            'container': self.buildContainer(Blog.objects.all(), SubscribeBlog.objects.filter(user_id = user_id))
        }
        return context

    def buildContainer(self, blogs, subscribeBlogs):
        """Построение контейнера, содержащего общий список блогов и статус (подписан, не подписан)"""
        status = []

        for val1 in range(0, len(blogs)):
            key = False
            for val2 in range(0, len(subscribeBlogs)):
                if (blogs[val1].id == subscribeBlogs[val2].blog_id):
                    status.append(True)
                    key = True
                    break
            if(key != True):
                status.append(False)

        return zip(blogs, status)


class PostsBlogView(TemplateView):
    """Список постов конкретного блога"""

    def get_context_data(self, blog_id):
        posts = Post.objects.filter(blog_id = blog_id)
        blog = Blog.objects.get(pk = blog_id)
        context = super(PostsBlogView, self).get_context_data()
        context = {
            'blog': blog,
            'posts': posts
        }
        return context


class AddPostView(CreateView):
    """Добавление нового поста"""

    form_class = PostForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        blog_id = self.kwargs['blog_id']
        if Blog.objects.get(pk = blog_id): # Если id блога найден, продолжить
            context = super(AddPostView, self).get_context_data(**kwargs)
            context['blog_id'] = blog_id
            return context
        else:  # Иначе вывести ошибку
            return Http404

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.blog_id = self.kwargs['blog_id']
        instance.save()
        return HttpResponseRedirect(self.success_url)


def AddSubscribeBlogView(self, user_id, blog_id):
    subscribe_blog = SubscribeBlog()
    subscribe_blog.user_id = user_id
    subscribe_blog.blog_id = blog_id
    subscribe_blog.save()
    return HttpResponseRedirect(reverse('blogs:tape_user', args = user_id))


def DelSubscribeBlogView(self, user_id, blog_id):
    subsctibe_blog = SubscribeBlog.objects.get(user_id = user_id, blog_id = blog_id)
    subsctibe_blog.delete()
    return HttpResponseRedirect(reverse('blogs:tape_user', args=user_id))

#def AddSubscribeBlogView(self, request, *args, **kwargs):

# class EditPostView(UpdateView):
#     """Редактирование поста"""
#
#     form_class = PostForm
#     # model = Post
#     success_url = '/'
#
#     def get_context_data(self, **kwargs):
#         context = super(EditPostView, self).get_context_data(**kwargs)
#         context['post_id'] = self.kwargs['post_id']
#         return context



