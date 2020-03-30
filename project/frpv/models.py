from django.db import models


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
        blank=True, null=True,
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

    def __str__(self):
        return "%s - ИНН %d : %d" % (self.name, self.INN, self.loan_amount)

    class Meta:
        ordering = ['name']
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
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата/время')
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
    header = models.CharField(blank=True, null=True, max_length=100, verbose_name='Заголовок')
    blockname = models.CharField(primary_key=True, max_length=50, verbose_name='Имя блока')
    text = models.TextField(verbose_name='Текст')
    group = models.CharField(blank=True, null=True, max_length=100, verbose_name='Группа (см. контекст)')
    attachment = models.FileField(upload_to='pdf/', max_length=500, blank=True, verbose_name='Вложение')
    image = models.ImageField(upload_to='img/', max_length=500, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.blockname

    class Meta:
        verbose_name_plural = "Данные сайта"
