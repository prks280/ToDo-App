from django.db import models


class Todo(models.Model):
    date = models.DateTimeField()
    name = models.TextField(max_length=255)
    deleted = models.BooleanField(default=False)



    def __str__(self):
        return '{} {}'.format(self.name,self.date)
