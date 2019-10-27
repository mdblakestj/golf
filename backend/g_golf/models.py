from django.db import models
from django.contrib.auth.models import User

class Hole(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    par = models.PositiveIntegerField()
    low_score = models.PositiveIntegerField()
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    par = models.PositiveIntegerField()
    low_score = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


    def __str__(self):
        return self.name


class CourseHole(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    hole = models.ForeignKey(Hole, on_delete=models.DO_NOTHING)




class Game(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    player_2_name = models.CharField(max_length=100)
    player_3_name = models.CharField(max_length=100)
    player_4_name = models.CharField(max_length=100)
    player_1_score = models.IntegerField(default=0)
    player_2_score = models.IntegerField(default=0)
    player_3_score = models.IntegerField(default=0)
    player_4_score = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    present_hole = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.created_at


class HoleInst(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    player_1_score = models.CharField(max_length=100)
    player_2_score = models.CharField(max_length=100)
    player_3_score = models.CharField(max_length=100)
    player_4_score = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


    def __str__(self):
        return self.created_at
