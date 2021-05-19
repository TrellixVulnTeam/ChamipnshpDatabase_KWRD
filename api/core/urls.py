from rest_framework import routers
from .views import ChampionshipViewSet, UserViewSet, ResultViewSet, DriverViewSet, TeamViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('championships', ChampionshipViewSet)
router.register(r'users', UserViewSet)
router.register(r'results', ResultViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = [
    path('', include(router.urls))
]