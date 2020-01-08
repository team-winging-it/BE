from django.conf.urls import url
from . import api
from rest_framework import routers
from .api import RoomViewSet, PlayerViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('rooms', RoomViewSet, 'rooms')
router.register('players', PlayerViewSet, 'players')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]
