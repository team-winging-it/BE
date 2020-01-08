from django.conf.urls import url
from . import api
from rest_framework import routers
from .api import RoomViewSet

router = routers.DefaultRouter()
router.register('rooms', RoomViewSet, 'rooms')

urlpatterns = router.urls


# urlpatterns = [
#     url('init', api.initialize),
#     url('move', api.move),
#     url('say', api.say),
# ]
