from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("login", login),
    path("join", join),
    path("board/write", board_form),
    path("board/<int:pk>", board),
]