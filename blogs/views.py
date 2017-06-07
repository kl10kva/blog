from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from .models import User, Blog, Post, SubscribeBlog, MarkPost
from .forms import PostForm


# class TapeUserView(TemplateView):
#     """Лента пользователя"""
#
#     def get_context_data(self, user_id):
#         #context = super(TapeUserView, self).get_context_data()
#         context = {
#             'user': User.objects.get(pk = user_id)
#         }
#         return context
class CreatePostView(CreateView):
    """Добавление нового поста"""
    form_class = PostForm
    success_url = '/'

