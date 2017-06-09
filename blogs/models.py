from django.db import models


class User(models.Model):
    """Информация о пользователях"""
    login = models.CharField(max_length = 40, unique = True, verbose_name = "Уникальное имя пользователя")
    first_name = models.CharField(max_length = 40, verbose_name = "Фамилия пользователя")
    last_name = models.CharField(max_length = 40, verbose_name = "Имя пользователя")
    email = models.EmailField(unique = True, verbose_name = "Адрес электронной почты")
    reg_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return "[%s, %s]: %s %s" % (self.login, self.email, self.first_name, self.last_name)


class Blog(models.Model):
    """Информация о блогах"""
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Пользователь",)
    title = models.CharField(max_length = 40, unique = True, verbose_name = "Наименование блога")
    description = models.TextField(verbose_name = "Описание блога")
    creation_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return "(%s): %s" % (self.creation_date, self.title)


class Post(models.Model):
    """Информация о постах"""
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Блог", )
    title = models.CharField(max_length = 40, unique = True, verbose_name = "Наименование поста")
    description = models.TextField(verbose_name = "Содержание поста")
    creation_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return "(%s). %s: %s" % (self.creation_date, self.blog, self.title)


class SubscribeBlog(models.Model):
    """Информация о подписках пользователей на блоги"""

    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Пользователь", )
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Блог",)

    def __str__(self):
        return "%s: %s (%s)" % (self.user, self.blog, self.status)


class MarkPost(models.Model):
    """Информация о помеченных пользователем постах"""

    # subscribe_blog = models.ForeignKey(SubscribeBlog, verbose_name = "Подписка", on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = "Пост", )
    user_id = models.PositiveIntegerField(null = True, blank = True, verbose_name = "ID пользователя")

    def __str__(self):
        return "%s: %s (%s)" % (self.subscribe_blog, self.post, self.status)

