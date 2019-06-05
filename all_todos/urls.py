from rest_framework import routers
from all_todos.views import *
from django.conf.urls import url
from django.urls import path


router = routers.SimpleRouter()

router.register(r'a',TodoViewSet)



# urlpatterns = router.urls


urlpatterns = [
    path('', TodoApi.as_view(), name='home'),
]