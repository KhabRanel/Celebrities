from django.db import models
from django.urls import reverse
from slugify import slugify


class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Stars.Status.PUBLISHED)


class Stars(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0
        PUBLISHED = 1

    name = models.CharField(max_length=30, verbose_name='Имя')
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    country = models.CharField(max_length=20, verbose_name='Страна')
    birth_date = models.DateField(blank=True, verbose_name='Дата рождения')
    content = models.TextField(blank=True, verbose_name='Краткая биография')
    full_content = models.TextField(blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True,
                              null=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Статус')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    objects = models.Manager()
    published = PublishedModel()

    def save(self, *args, **kwargs):
        if not self.content:
            self.content = self.__cut_content()
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Stars.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)


    def __cut_content(self):
        text = ''
        count = 0
        for x in self.full_content:
            if count < 2:
                text += x
                if x == '.':
                    count += 1
            else:
                break
        return text

    def get_absolute_url(self):
        return reverse('person', kwargs={'person_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

        verbose_name = 'Знаменитости'
        verbose_name_plural = 'Знаменитости'

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'




