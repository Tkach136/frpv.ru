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


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['-date']

    def __str__(self):
        return self.text[:100] + '...'
