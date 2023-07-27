from django.urls import path
from .views import get_board_all

urlpatterns = [
    path('', get_board_all),
    path('board', get_board_all),
]