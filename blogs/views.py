from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings

from .forms import PostForm
from .models import User, Blog, Post, SubscribeBlog, MarkPost


class TapeUserView(TemplateView):
    """Профиль пользователя"""

    def get_context_data(self, user_id):
        context = super(TapeUserView, self).get_context_data()

        my_blog = Blog.objects.get(user_id = user_id)
        subscribeBlogs = SubscribeBlog.objects.filter(user_id = user_id)
        containerBlogs = self.buildContainerBlogs(Blog.objects.all(), subscribeBlogs)
        containerPosts = self.buildContainerPosts(subscribeBlogs, Post.objects.all(), my_blog)

        context = {
            'my_blog': my_blog,
            'containerBlogs': containerBlogs,
            'containerPosts': containerPosts
        }
        return context

    def buildContainerBlogs(self, blogs, subscribeBlogs):
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

    def buildContainerPosts(self, subscribeBlogs, allPosts, my_blog):
         """Построение контейнера, содержащего общий список постов блогов
            на которые подписан пользователь, а так же их статусы (прочтено, не прочтено)"""
         posts = []

         for elem in subscribeBlogs:
            for val in range(0, len(allPosts)):
                if (elem.blog_id == allPosts[val].blog_id and elem.blog_id != my_blog.id):
                    posts.append(allPosts[val])

         markPosts = MarkPost.objects.all()
         status = []

         for val1 in range(0, len(posts)):
             key = False
             for val2 in range(0, len(markPosts)):
                 if (posts[val1].id == markPosts[val2].post_id):
                     status.append(True)
                     key = True
                     break
             if (key != True):
                 status.append(False)

         return zip(posts, status)


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
        blog_id = self.kwargs['blog_id']
        instance = form.save(commit = False)
        instance.blog_id = blog_id
        instance.save()

        subscribe_blogs = SubscribeBlog.objects.filter(blog_id = blog_id)

        for elem in subscribe_blogs:
            user = User.objects.get(pk = elem.user_id)
            blog = Blog.objects.get(pk = blog_id)
            send_mail('NewPost', 'Опубликован новый пост. Блог: ' + str(blog.title), settings.EMAIL_HOST_USER, [user.email])

        return HttpResponseRedirect(self.success_url)


def AddSubscribeBlogView(self, user_id, blog_id):
    """Добавление подписки"""
    subscribe_blog = SubscribeBlog()
    subscribe_blog.user_id = user_id
    subscribe_blog.blog_id = blog_id
    subscribe_blog.save()
    return HttpResponseRedirect(reverse('blogs:tape_user', args = user_id))


def DelSubscribeBlogView(self, user_id, blog_id):
    """Снятие подписки с блога"""
    subsctibe_blog = SubscribeBlog.objects.get(user_id = user_id, blog_id = blog_id)
    subsctibe_blog.delete()
    mark_posts = MarkPost.objects.filter(user_id = user_id)
    mark_posts.delete()
    return HttpResponseRedirect(reverse('blogs:tape_user', args = user_id))


def MarkPostView(self, post_id, user_id):
    """Пометить пост как 'Прочитано'"""
    mark_posts = MarkPost()
    mark_posts.post_id = post_id
    mark_posts.user_id = user_id
    mark_posts.save()
    return HttpResponseRedirect(reverse('blogs:tape_user', args = user_id))

