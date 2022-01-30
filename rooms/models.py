from django.db import models

# Create your models here.

class Rooms(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField(default=0)
    columns = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Walls(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    room = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)

class Lightbulbs(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    room = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)