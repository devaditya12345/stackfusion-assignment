from django.urls import path

from .views import UserViewSet


urlpatterns = [
    path("user-form/", UserViewSet.as_view()),
]
