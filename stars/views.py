import json
from django.core.serializers import serialize
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from stars.models import Stars, Category
from .forms import AddPostForm
from django.http import (HttpResponse, HttpResponseNotFound, HttpResponseServerError,
                         HttpResponseForbidden, HttpResponseBadRequest)
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


class StarsHome(ListView):
    template_name = 'stars/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_celebrities'] = self.__get_all_celebrities()
        context['celebrities'] = Stars.published.all()[:4]
        context['birthday_celebrities'] = self.__get_birthday_celebrities()
        return context

    @staticmethod
    def get_queryset():
        return Stars.published.all().select_related('cat')

    @staticmethod
    def __get_all_celebrities():
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
        return all_celebrities

    @staticmethod
    def __get_birthday_celebrities():
        today = date.today()
        birthday_celebrities = Stars.published.filter(
            birth_date__month=today.month,
            birth_date__day=today.day)
        return birthday_celebrities


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'stars/addpage.html'
    success_url = reverse_lazy('home')


class ShowPerson(DetailView):
    model = Stars
    template_name = 'stars/person.html'
    context_object_name = 'post'
    slug_url_kwarg = 'person_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].name
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Stars.published, slug=self.kwargs[self.slug_url_kwarg])


class StarsCategory(ListView):
    template_name = 'stars/category.html'
    context_object_name = 'person'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['person'][0].cat
        context['title'] = f'Знаменитости из сферы {category.name}'
        return context

    def get_queryset(self):
        return Stars.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


def about(request):
    return render(request, 'stars/about.html')

def login(request):
    return render(request, 'stars/login.html')


# Обработка  ошибок

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def server_error(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')

def permission_denied(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>')

def bad_request(request, exception):
    return HttpResponseBadRequest('<h1>Невозможно обработать запрос</h1>')