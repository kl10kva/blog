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
    user = models.ForeignKey(User, verbose_name = "Пользователь", on_delete = models.CASCADE)
    title = models.CharField(max_length = 40, unique = True, verbose_name = "Наименование блога")
    description = models.TextField(verbose_name = "Описание блога")
    creation_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return "(%s): %s" % (self.creation_date, self.title)


class Post(models.Model):
    """Информация о постах"""
    blog = models.ForeignKey(Blog, verbose_name = "Блог", on_delete = models.CASCADE)
    title = models.CharField(max_length = 40, unique = True, verbose_name = "Наименование поста")
    description = models.TextField(verbose_name = "Содержание поста")
    creation_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return "(%s). %s: %s" % (self.creation_date, self.blog, self.title)


class SubscribeBlog(models.Model):
    """Информация о подписках пользователей на блоги"""
    NOT_SIGNED = False
    SIGNED = True
    STATUS = (
        (NOT_SIGNED, "Не подписан"),
        (SIGNED, "Подписан")
    )
    user = models.ForeignKey(User, verbose_name = "Пользователь", on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name = "Блог", on_delete = models.CASCADE)
    status = models.BooleanField(choices = STATUS, verbose_name = "Статус подписки")

    def __str__(self):
        return "%s: %s (%s)" % (self.user, self.blog, self.status)


class MarkPost(models.Model):
    """Информация о помеченных пользователем постах"""
    NOT_READ = False
    READ = True
    STATUS = (
        (NOT_READ, "Не прочитано"),
        (READ, "Прочитано")
    )
    subscribe_blog = models.ForeignKey(SubscribeBlog, verbose_name = "Подписка", on_delete = models.CASCADE)
    post = models.ForeignKey(Post, verbose_name = "Пост", on_delete = models.CASCADE)
    status = models.BooleanField(choices = STATUS, verbose_name = "Статус")

    def __str__(self):
        return "%s: %s (%s)" % (self.subscribe_blog, self.post, self.status)

