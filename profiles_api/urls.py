from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()

router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")

urlpatterns = [
    path("hello-api", views.HelloWorldApi.as_view()),
    path("", include(router.urls))
]