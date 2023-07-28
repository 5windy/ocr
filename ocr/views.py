from django.shortcuts import render

def index(request) :
    return render(request, 'index.html')

def login(request) :
    return render(request, 'login_form.html')

def join(request) :
    return render(request, 'join_form.html')

def board(request) :
    return render(request, 'board_form.html')
