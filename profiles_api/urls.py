from django.urls import path
from profiles_api import views

urlpatterns = [
    path("hello-api", views.HelloWorldApi.as_view()),
]