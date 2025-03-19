import json
from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404, redirect
from stars.models import Stars, Category
from .forms import AddPostForm
from django.http import (HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseBadRequest)
from datetime import date

MONTHS = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря",
    }

def index(request):

    today = date.today()

    birthday_celebrities = Stars.published.filter(
        birth_date__month=today.month,
        birth_date__day=today.day)

    celebrities = Stars.published.all()[:4]

    all_celebrities = []
    for star in Stars.published.all():
        day = str(star.birth_date.day)
        month = MONTHS[star.birth_date.month]
        formatted_date = f"{day} {month} {star.birth_date.year} г."
        all_celebrities.append({
            'name': star.name,
            'slug': star.get_absolute_url(),
            'country': star.country,
            'birth_date': formatted_date,
            'content': star.content,
            'cat': star.cat.name,
        })

    data = {
        'celebrities': celebrities,
        'birthday_celebrities': birthday_celebrities,
        'all_celebrities': all_celebrities
    }
    return render(request, 'stars/index.html', context=data)

def about(request):
    return render(request, 'stars/about.html')

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'form': form
    }
    return render(request, 'stars/addpage.html', context=data)

def login(request):
    return render(request, 'stars/login.html')

def show_person(request, person_slug):
    person = get_object_or_404(Stars, slug=person_slug)
    data = {
        'title': person.name,
        'post': person,
        'cat_selected': 1,
    }
    return render(request, 'stars/person.html', context=data)

def show_categories(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    person = Stars.published.filter(cat_id=category.pk)
    data = {
        'category': category,
        'person': person,
        'title': f'Знаменитости из сферы {category.name}'
    }
    return render(request, 'stars/category.html', context=data)

# Обработка  ошибок

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def server_error(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')

def permission_denied(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>')

def bad_request(request, exception):
    return HttpResponseBadRequest('<h1>Невозможно обработать запрос</h1>')