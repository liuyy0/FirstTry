from django.db import models


# 出版社表
class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)


# 书表
class Books(models.Model):
    name = models.CharField(max_length=32, unique=True)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)


# 作者表
class Authors(models.Model):
    name = models.CharField(max_length=32,unique=True)
    books = models.ManyToManyField('Books',through='AuthorBook')


class AuthorBook(models.Model):
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    book = models.ForeignKey('Books', on_delete=models.CASCADE)
    date = models.DateTimeField()
