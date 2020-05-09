from django.db import models
from django.utils import timezone


class Bid(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='наименование')
    OGRN = models.IntegerField(verbose_name='ОГРН')
    INN = models.IntegerField(
        verbose_name='ИНН')
    chief = models.CharField(
        max_length=100,
        verbose_name='руководитель')
    email = models.EmailField(
        verbose_name='email')
    target = models.TextField(
        verbose_name='цель и краткое описание')
    price_project = models.FloatField(
        verbose_name='стоимость проекта')
    implementation_period = models.CharField(
        max_length=100,
        verbose_name='срок реализации проекта')
    sum_of_self_investments = models.FloatField(
        verbose_name='сумма собственных вложений')
    loan_amount = models.FloatField(
        verbose_name='сумма займа')
    term_use_of_the_loan = models.SmallIntegerField(
        verbose_name='срок пользования займа (месяцев)')
    proposed_collateral = models.CharField(
        max_length=200,
        verbose_name='предлагаемое обеспечение')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время оставления заявки',
    )

    def __str__(self):
        return "( %s ) № %d от %s - ИНН %d" % (self.date, self.id, self.name, self.INN)

    class Meta:
        # ordering = ['-date']
        verbose_name_plural = 'Оставленные заявки'
        verbose_name = 'Заявка'


class Topic(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тема')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Темы новостей'
        verbose_name = 'Тема'


class Entry(models.Model):
    """Модель одной новости"""
    header = models.CharField(max_length=50, blank=True, null=True, verbose_name='Заголовок')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', editable=False)
    changed = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    attachment = models.FileField(upload_to='pdf/', max_length=500, blank=True, verbose_name='Вложение')
    image = models.ImageField(upload_to='img/', max_length=500, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-date']

    def __str__(self):
        return self.text[:200] + '...'


class Info(models.Model):
    """Модель информации на сайте"""
    page = models.CharField(max_length=200, blank=True, null=True, verbose_name='Страница')
    header = models.CharField(blank=True, null=True, max_length=100, verbose_name='Заголовок')
    blockname = models.CharField(primary_key=True, max_length=50, verbose_name='Имя блока')
    text = models.TextField(verbose_name='Текст')
    group = models.CharField(blank=True, null=True, max_length=100, verbose_name='Группа (см. контекст)')
    price = models.CharField(blank=True, null=True, max_length=20, 
                             verbose_name='Сумма займа (млн. руб)',
                             help_text='только для реализованных проектов')
    attachment = models.FileField(upload_to='pdf/', max_length=500, blank=True, verbose_name='Вложение')
    image = models.ImageField(upload_to='img/', max_length=500, blank=True, verbose_name='Изображение')

    def __str__(self):
        return "Группа %s , блок %s" % (self.group, self.blockname)

    class Meta:
        verbose_name_plural = "Данные сайта"
        ordering = ['page', 'header']
