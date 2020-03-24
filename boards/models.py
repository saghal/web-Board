from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 100)
class Topic(models.Model):
    subject = models.CharField(max_length = 255)
    last_updated = models.DateTimeField(auto_now = True)
    board = models.ForeingKey(Board,on_delete=CASCADE)
