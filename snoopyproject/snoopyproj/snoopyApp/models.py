from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=30)
    imageName = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Post(models.Model):
    description = models.CharField(max_length=512)
    characters = models.ManyToManyField(Character)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.description


class Comment(models.Model):
    content = models.CharField(max_length=512)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def delete_comment(self):
        self.delete()


