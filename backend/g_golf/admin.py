from django.contrib import admin

# Register your models here.

from .models import Hole, HoleInst, Game, Course, CourseHole

admin.site.register(HoleInst)
admin.site.register(Hole)
admin.site.register(Game)
admin.site.register(Course)
admin.site.register(CourseHole)
