from django.db import models


class Post(models.Model):  # class is the table, each field is col in table

    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
