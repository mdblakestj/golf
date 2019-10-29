from rest_framework import serializers
from g_golf.models import Game
from g_golf.models import Hole
from g_golf.models import Course
from g_golf.models import HoleInst
from g_golf.models import CourseHole


class HoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hole
        fields = ('id','creator', 'description','name', 'created_at', 'updated_at',
        'par', 'low_score', 'long', 'lat')



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','creator', 'description','name', 'created_at', 'updated_at',
        'par', 'low_score')




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'creator', "course", "player_2_name", "player_3_name",
         "player_4_name", "player_1_score", "player_2_score", "player_3_score",
         "player_4_score", "created_at", "updated_at", "present_hole")



class HoleInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoleInst
        fields = ('id', 'game', "hole", "player_1_score", "player_2_score", "player_3_score",
         "player_4_score", "created_at", "updated_at")




class CourseHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseHole
        fields = '__all__'

    # def create(self, validated_data):
    #     return CourseHole.objects.create(**validated_data)
