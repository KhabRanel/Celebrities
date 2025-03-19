from django.core.management.base import BaseCommand
from stars.models import Stars
from datetime import datetime


class Command(BaseCommand):
    help = 'Добавляет знаменитостей в базу данных'

    def handle(self, *args, **kwargs):
        celebrities = [
            {
                'name': 'Дженнифер Лоуренс',
                'slug': 'jennifer-lawrence',
                'country': 'США',
                'category': 'Кино',
                'birth_date': '1990-08-15',
                'content': 'Американская актриса, известная по фильмам "Голодные игры" и "Люди Икс".',
                'is_published': True,
                'cat_id': 1
            },
            {
                'name': 'Криштиану Роналду',
                'slug': 'cristiano-ronaldo',
                'country': 'Португалия',
                'category': 'Спорт',
                'birth_date': '1985-02-05',
                'content': 'Португальский футболист, один из лучших игроков в истории футбола.',
                'is_published': True,
                'cat_id': 3
            },
            {
                'name': 'Тейлор Свифт',
                'slug': 'taylor-swift',
                'country': 'США',
                'category': 'Музыка',
                'birth_date': '1989-12-13',
                'content': 'Американская певица и автор песен, известная своими альбомами в жанре поп и кантри.',
                'is_published': True,
                'cat_id': 2
            },
            {
                'name': 'Роберт Дауни мл.',
                'slug': 'robert-downey-jr',
                'country': 'США',
                'category': 'Кино',
                'birth_date': '1965-04-04',
                'content': 'Американский актер, известный по роли Тони Старка в фильмах Marvel.',
                'is_published': True,
                'cat_id': 1
            },
            {
                'name': 'Ариана Гранде',
                'slug': 'ariana-grande',
                'country': 'США',
                'category': 'Музыка',
                'birth_date': '1993-06-26',
                'content': 'Американская певица и актриса, известная своими хитами и вокальным диапазоном.',
                'is_published': True,
                'cat_id': 2
            },
            {
                'name': 'Лионель Месси',
                'slug': 'lionel-messi',
                'country': 'Аргентина',
                'category': 'Спорт',
                'birth_date': '1987-06-24',
                'content': 'Аргентинский футболист, считающийся одним из величайших игроков всех времен.',
                'is_published': True,
                'cat_id': 3
            },
            {
                'name': 'Скарлетт Йоханссон',
                'slug': 'scarlett-johansson',
                'country': 'США',
                'category': 'Кино',
                'birth_date': '1984-11-22',
                'content': 'Американская актриса, известная по роли Черной Вдовы в фильмах Marvel.',
                'is_published': True,
                'cat_id': 1
            },
            {
                'name': 'Дрейк',
                'slug': 'drake',
                'country': 'Канада',
                'category': 'Музыка',
                'birth_date': '1986-10-24',
                'content': 'Канадский певец и автор песен, один из самых популярных артистов в мире.',
                'is_published': True,
                'cat_id': 2
            },
            {
                'name': 'Эмма Уотсон',
                'slug': 'emma-watson',
                'country': 'Великобритания',
                'category': 'Кино',
                'birth_date': '1990-04-15',
                'content': 'Британская актриса, известная по роли Гермионы Грейнджер в серии фильмов о Гарри Поттере.',
                'is_published': True,
                'cat_id': 1
            },
            {
                'name': 'Канье Уэст',
                'slug': 'kanye-west',
                'country': 'США',
                'category': 'Музыка',
                'birth_date': '1977-06-08',
                'content': 'Американский рэпер, продюсер и дизайнер, известный своими альбомами и скандалами.',
                'is_published': True,
                'cat_id': 2
            }
        ]

        for data in celebrities:
            Stars.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Знаменитости успешно добавлены!'))
