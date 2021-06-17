from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name + ":" + self.email

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    views = models.IntegerField()
    reactions = models.IntegerField()

    def __str__(self):
        return "Title:" + self.title + ", Views:" + str(self.views) + ", reactions:" + str(self.reactions)
    
class Comment(models.Model):
    section = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text