from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Board

def say_hello(request) :
    return render(request, "index.html", {
        "data" : Board.objects.all()
    }) 

@api_view(['GET', 'POST'])
def get_board_all(request) :
    boards = Board.objects.all()
    # -> Board를 JSON으로 형변환 (Serializer)
    return Response({
        "data" : boards
    })