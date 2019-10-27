
from g_golf.models import Game, Course, HoleInst, CourseHole, Hole
from g_golf.serializers import (
    HoleSerializer,
    GameSerializer,
    CourseHoleSerializer,
    CourseSerializer,
    HoleInstSerializer
)
from rest_framework import viewsets



class GameView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class HoleInstView(viewsets.ModelViewSet):
    queryset = HoleInst.objects.all()
    serializer_class = HoleInstSerializer

class HoleView(viewsets.ModelViewSet):
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer


class CourseHoleView(viewsets.ModelViewSet):
    queryset = CourseHole.objects.all()
    serializer_class = CourseHoleSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Create your views here.
