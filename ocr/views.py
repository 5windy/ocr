from django.shortcuts import render

def index(request) :
    return render(request, 'index.html')

def login(request) :
    return render(request, 'login_form.html')

def join(request) :
    return render(request, 'join_form.html')

def board(request, pk) :
    return render(request, 'board.html')

def boards(request) :
    return render(request, 'board_list.html')

def board_form(request) :
    return render(request, 'board_form.html')
