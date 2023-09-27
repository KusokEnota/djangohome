from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = """
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой Django-сайт!</h1>
        <p>Это главная страница сайта.</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Меня зовут Денис.я студент GB :).</p>
    </body>
    </html>
    """
    return HttpResponse(html)
