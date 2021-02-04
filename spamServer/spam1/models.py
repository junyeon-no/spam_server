from django.db import models

# Create your models here.

class Blog(models.Model):
    Title = models.CharField('TITLE', max_length = 50)
    contest = models.TextField('content')

    def __str__(self):
        return self.Title

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()



