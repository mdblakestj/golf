from django.db import models
from django.contrib.auth.models import User

class Base(object):
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)




# class MBase(models.Model):
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
# Django requires you to designate this as some kind of abstract
#lookup correct way to do this.
class Hole(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    name = models.CharField(max_length=100)
    par = models.PositiveIntegerField()
    low_score = models.PositiveIntegerField()
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


    def __str__(self):
        return self.name


class Course(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    player_2_name = models.CharField(max_length=100)
    player_3_name = models.CharField(max_length=100)
    player_4_name = models.CharField(max_length=100)
    player_1_score = models.IntegerField(default=0)
    player_2_score = models.IntegerField(default=0)
    player_3_score = models.IntegerField(default=0)
    player_4_score = models.IntegerField(default=0)
    present_hole = models.PositiveIntegerField(default=1)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


    def __str__(self):
        return self.created_at

    # def get_scores(self):
    #     return [(x.player.name, x.hole.number, x.score) for x in self.scores]

# class PlayerScore()
#     game = models.ForiegnKey(related_name="scores") #related name sets up reverse relationship see: django many to many foreign key
#     hole = models.ForeignKey(related_name="hole_scores")
#     player =
#     score = models.IntegerField

    # def get_course_name(self):
    #     return self.game.course.id
    #
    # def get_all_courses_named(self, namequery):
    #     return self.objects.filter(game__course__name__like__=namequery)




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
