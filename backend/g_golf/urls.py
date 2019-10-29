from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('games', views.GameView)
router.register('hole', views.HoleView)
router.register('course', views.CourseView)
router.register('holeinst', views.HoleInstView)
router.register('coursehole', views.CourseHoleView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
