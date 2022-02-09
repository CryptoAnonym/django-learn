from rest_framework import routers
from .views import VoteViewSet, IdeaViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r"ideas", IdeaViewSet)
router.register(r"votes", VoteViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))

]
