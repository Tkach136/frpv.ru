from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, response, JsonResponse
from django.views import generic
from . models import Bid
from django.core.mail import EmailMessage, send_mail
from django.core import mail
from django.conf import settings
from django_db_logging import logging
from django.utils import timezone
import json
from pprint import pformat

labels = ('name', 'OGRN', 'INN', 'chief', 'email', 'target',
          'price_project', 'implementation_period', 'sum_of_self_investments',
          'loan_amount', 'term_use_of_the_loan', 'proposed_collateral',
          )

FORM = """
Наименование организации: $VALUE$
ОГРН: $VALUE$
ИНН: $VALUE$
Руководитель (ФИО, телефон): $VALUE$ 
email: $VALUE$ 
Цель и краткое описание проекта: $VALUE$
Общая стоимость проекта: $VALUE$ 
Срок реализации проекта: $VALUE$ 
Сумма собственных вложений: $VALUE$
Сумма запрашиваемого займа: $VALUE$
Срок пользования займа(месяцев): $VALUE$ 
Предлагаемое обеспечение: $VALUE$
"""

ROWS = {
    'name': 'Наименование организации',
    'OGRN': 'ОГРН',
    'INN': 'ИНН',
    'chief': 'Руководитель (ФИО, телефон)',
    'email': 'email',
    'target': 'Цель и краткое описание проекта',
    'price_project': 'Общая стоимость проекта',
    'implementation_period': 'Срок реализации проекта',
    'sum_of_self_investments': 'Сумма собственных вложений',
    'loan_amount': 'Сумма запрашиваемого займа',
    'term_use_of_the_loan': 'Срок пользования займа(месяцев)',
    'proposed_collateral': 'Предлагаемое обеспечение',
}

msg = """
Заявка %s успешно создана! 
Наши менеджеры свяжутся с Вами в самое ближайшее время. 
С уважением, Региональный фонд развития промышленности Воронежской области.
"""


def test_send(request):
    if request.method != 'POST':
        return HttpResponse('Вы ввели некорректные данные. Пожалуйста, попробуйте ещё раз.')
    elif request.method == 'POST':
        data = request.POST.get('test')
        # data = json.loads(data)
        send_mail('topic', data,
                  settings.EMAIL_HOST_USER,
                  ['egrazor@yandex.ru']
                  )
        return HttpResponse(data)


def index(request):
    content = request.headers.items()
    return HttpResponse(content)


def application(request):
    context = {'labels': labels}
    return render(request, 'frpv/application.html', context)


def send(request):
    if request.method != 'POST':
        return HttpResponse('Заполните недостающие поля.')
    elif request.method == 'POST':
        data = request.POST
        bid = Bid(
            name=data.get('name'),
            OGRN=data.get('OGRN'),
            INN=data.get('INN'),
            chief=data.get('chief'),
            email=data.get('email'),
            target=data.get('target'),
            price_project=data.get('price_project'),
            implementation_period=data.get('implementation_period'),
            sum_of_self_investments=data.get('sum_of_self_investments'),
            loan_amount=data.get('loan_amount'),
            term_use_of_the_loan=data.get('term_use_of_the_loan'),
            proposed_collateral=data.get('proposed_collateral')
        )
        bid.save()
        now = timezone.now()
        topic = 'Заявка № %s компании %s , ИНН %s' % (bid.id, bid.name, bid.INN)
        # TODO косяки со временем. Логи добавить
        # logging('%s была создана' % now +
        #         topic + 'на сумму %s' % bid.loan_amount)
        email_body = ''
        for (key, value) in ROWS.items():
            row = value + ' : ' + data.get('%s' % key) + '\n'
            email_body += row
        send_mail(topic, email_body,
                  settings.EMAIL_HOST_USER,
                  ['egrazor@yandex.ru'])
        # TODO добавить отправку письма о создании заявки юзеру
        return HttpResponse(msg % bid.id)
    else:
        return HttpResponse('Вы ввели некорректные данные. Пожалуйта, попробуйте ещё раз.')



