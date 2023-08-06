from django.db import models

# Create your models here.

class Author(models.Models):
    full_name = models.CharField(max_length=64) # полное имя автора
    name = models.CharField(null=True, max_length=64)
    rate = models.IntegerField(default=0.0) #рейтинг

    def update_rating(self):
        #как это умножать на 3, не понимаю для чего
        #немного не понял задания,надо возвращать суммарный рейтинг или обновлять как-то?
        #тоже самое

class Category(models.Model):
    name_of_category = models.CharField(max_length=100,unique=True)#название категории и ее уникальность

class Post(models.Models):
    author = models.ForeignKey(Author,on_delete=models.CASCADE) #связь один ко многим с автором
    #поле с выбором новости или статьи?

    time_of_add = models.DateTimeField(auto_now_add=True) #время добавления
    postcat = models.ManyToManyField(PostCategory)#связь с доп моделью посткатегори
    header = models.CharField(max_length=100)#заголовок статьи
    text_of_news = models.CharField()#текст
    rate_of_news = models.IntegerField(default=0.0) #рейтинг статьи

    def like(self):
        self.rate_of_news += 1 #не уверен правильно ли

    def dislike(self):
        self.rate_of_news -= 1#так же неуверен

    def preview(self,text_of_news):
        return #как вернуть начало статьи?



class PostCategory(models.Models):
    post = models.ManyToManyField(Post)#связь многи ко многим с пост
    category = models.ManyToManyField(Category)

class Comment(models.Model):
    post_2 = models.ManyToManyField(Post)#связь с пост
    #не знаю как сделать связь многие ко многим с моделью User

    text_of_comm = models.CharField(max_length=800)#текст комментария
    time_of_comm = models.DateTimeField(auto_now_add=True)#время добавления
    rate_of_comm = models.IntegerField(default=0.0)#рейтинг

    def like(self):
        self.rate_of_comm += 1 #не уверен в правильности данного метода

    def dislike(self):
        self.rate_of_comm -= 1 #так же не уверен










