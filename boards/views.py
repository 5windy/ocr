# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Board
from .serializers import BoardSerializer

def say_hello(request) :
    return render(request, "index.html", {
        "data" : Board.objects.all()
    }) 

# @api_view(['GET', 'POST'])
# def get_board_all(request) :
#     boards = Board.objects.all()
#     # -> Board를 JSON으로 형변환 (Serializer)
#     serializer = BoardSerializer(boards, many=True)
#     return Response(serializer.data)

class Boards(APIView) :
    def get(self, request) :
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    
    def post(self, request) :
        pass


class BoardDetail(APIView) :
    def get(self, request) :
        pass

    def put(self, request) :
        
        pass
    def delete(self, request) :
        pass